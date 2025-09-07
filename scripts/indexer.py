import os
import pathlib
import json
import re
import yaml
from concurrent.futures import ThreadPoolExecutor, as_completed
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

ACRONYMS = {"AI", "API", "HTTP", "HTTPS", "SQL", "JSON", "XML", "CPU", "GPU", "OAuth", "CLI", "URL", "DNS", "IP", "UI", "MCP"}

CLUSTERS = {
    "All Content": [],
    "AI Builder": ["ai_builder"],
    "Hosting": ["hosting"],
    "Components": ["custom-components", "recipes"],
    "Enterprise": ["enterprise"],
    "API Reference": ["api-reference", "api-routes"],
    "Docs": ["advanced_onboarding", "assets", "authentication", "client_storage", "components", "database", "events", "getting_started", "library", "pages", "state", "state_structure", "styling", "ui", "utility_methods", "vars", "wrapping-react"],
    "Blog Posts": []
}


def smart_title_case(name: str) -> str:
    def fix_word(word: str) -> str:
        return word.upper() if word.upper() in ACRONYMS else word.capitalize()
    return " ".join(fix_word(w) for w in name.split())

def clean_name(name: str) -> str:
    if name.lower().endswith(".md"):
        name = name[:-3]
    name = name.replace("_", " ").replace("-", " ").strip()
    return smart_title_case(name)


def clean_markdown(text: str) -> str:
    text = re.sub(r"^---[\s\S]*?---\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"<div[\s\S]*?</div>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"`[^`]+`", "", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    return text.strip()


def extractive_summary(text: str, sentence_count: int = 2) -> str:
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)

def summarize_markdown(md_path: str, max_lines: int = 7) -> str:
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    cleaned = clean_markdown(content)

    # Split into lines and keep only first max_lines lines
    lines = cleaned.splitlines()
    truncated_lines = lines[:max_lines]
    truncated_text = "\n".join(truncated_lines).strip()

    # If short, return as is
    if len(truncated_lines) < max_lines:
        return truncated_text

    # Optionally add ellipsis if truncated
    return truncated_text + "\n..."


def name_from_url(url: str) -> str:
    parts = url.strip("/").split("/")
    if parts[0] == "docs":
        parts = parts[1:]
    # Patch last part from 'low' to 'Low Level'
    if parts and parts[-1] == "low":
        parts[-1] = "low-level"
    readable = " ".join(part.replace("-", " ") for part in parts)
    return smart_title_case(readable)

def process_file(docs_path: str, file: str, root: str) -> dict:
    file_path = os.path.join(root, file)
    rel_path = os.path.relpath(file_path, docs_path)
    parts = pathlib.Path(rel_path).parts

    # Strip extension for the last part
    filename_no_ext = file.rsplit(".", 1)[0]

    # Build parts_clean, replacing final LL cases properly
    parts_clean = []
    for i, p in enumerate(parts):
        is_last = i == len(parts) - 1
        if is_last:
            if filename_no_ext.endswith("-ll"):
                parts_clean.append("Low Level")
            else:
                parts_clean.append(clean_name(filename_no_ext))
        else:
            parts_clean.append(clean_name(p))

    # Patch URL from "something-ll.md" → "something/low"
    url_parts = [p.replace("_", "-").rsplit(".", 1)[0] for p in parts]
    if url_parts and url_parts[-1].endswith("-ll"):
        url_parts[-1] = url_parts[-1].replace("-ll", "/low")

    url = "/" + "/".join(url_parts)
    name = name_from_url(f"docs{url}")
    description = summarize_markdown(file_path)

    parent = parts[0] if parts else ""
    cluster = "Uncategorized"
    for cluster_name, folder_list in CLUSTERS.items():
        if parent in folder_list:
            cluster = cluster_name
            break

    return {
        "name": name,
        "parts": parts_clean,
        "url": f"docs{url}",
        "cluster":cluster,
        "description": description,
    }

def build_docs_index(docs_path: str, max_workers: int = 4) -> list:
    files_to_process = []
    for root, _, files in os.walk(docs_path):
        for file in files:
            if file.endswith(".md"):
                files_to_process.append((docs_path, file, root))

    index = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_file, *args) for args in files_to_process]
        for future in as_completed(futures):
            index.append(future.result())
    return index

if __name__ == "__main__":
    docs_dir = "docs"
    index = build_docs_index(docs_dir, max_workers=4)
    output_path = "pcweb/components/docpage/navbar/docs_index.py"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# This file was dynamically generated. DO NOT EDIT.\n\n")
        f.write("indexed_docs = ")
        json.dump(index, f, indent=2, ensure_ascii=False)
    print(f"Indexed {len(index)} documents. Output written to {output_path}")


def extract_frontmatter(md_path: str) -> dict:
    """Extract YAML frontmatter from a markdown file."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}

    try:
        frontmatter = yaml.safe_load(match.group(1))
        return frontmatter
    except yaml.YAMLError:
        return {}


def slugify(filename: str) -> str:
    name = pathlib.Path(filename).stem
    return name.lower().replace("_", "-")


def process_blog_file(blog_root: str, file: str, root: str) -> dict | None:
    file_path = os.path.join(root, file)
    fm = extract_frontmatter(file_path)

    if not fm or not all(k in fm for k in ("title", "author", "date", "description", "image")):
        return None

    rel_path = os.path.relpath(file_path, blog_root)
    slug = slugify(rel_path)
    url = f"/blog/{slug}"

    return {
        "title": fm["title"],
        "url": url,
        "author": fm["author"],
        "date": str(fm["date"]),
        "description": fm["description"],
        "image": fm["image"],
    }


def build_blog_index(blog_path: str, max_workers: int = 4) -> list:
    files_to_process = []
    for root, _, files in os.walk(blog_path):
        for file in files:
            if file.endswith(".md"):
                files_to_process.append((blog_path, file, root))

    index = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_blog_file, *args) for args in files_to_process]
        for future in as_completed(futures):
            result = future.result()
            if result:
                index.append(result)

    return sorted(index, key=lambda b: b["date"], reverse=True)


if __name__ == "__main__":
    blog_dir = "blog"
    index = build_blog_index(blog_dir)

    output_path = "pcweb/components/docpage/navbar/blog_index.py"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# This file was dynamically generated. DO NOT EDIT.\n\n")
        f.write("indexed_blogs = ")
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"Indexed {len(index)} blog posts. Output written to {output_path}")
