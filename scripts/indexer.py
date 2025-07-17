# import os
# import re
# import pathlib
# from typing import List, Dict

# from transformers import pipeline

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# def summarize_markdown_local(md_path: str) -> str:
#     with open(md_path, "r", encoding="utf-8") as f:
#         content = f.read()

#     # Transformers have max token limits (~1024 tokens), so truncate
#     truncated = content[:1024]

#     summary = summarizer(truncated, max_length=47, min_length=20, do_sample=False)
#     return summary[0]['summary_text']


# def extract_description(md_path: str, max_lines: int = 3) -> str:
#     """Extract a meaningful paragraph from a Markdown file for use as a description."""
#     with open(md_path, "r", encoding="utf-8") as f:
#         lines = [line.strip() for line in f if line.strip()]

#     for line in lines:
#         # Skip frontmatter, comments, headings, and lists
#         if (
#             line.startswith("---")
#             or line.startswith("<!--")
#             or line.startswith("#")
#             or line.startswith(("*", "-", "+"))
#             or line.startswith(">")
#         ):
#             continue

#         # Only return real sentences (not links, code blocks, etc.)
#         if len(line) > 30 and not re.match(r"^\[.*\]\(.*\)$", line):
#             return line

#     # fallback to first heading if no better content
#     for line in lines:
#         if line.startswith("#"):
#             return re.sub(r"#* ?", "", line)

#     return ""



# def clean_name(name: str) -> str:
#     """Clean file name by stripping extension and replacing underscores."""
#     return name.replace("_", " ").rsplit(".", 1)[0].strip()


# def build_docs_index(docs_path: str) -> List[Dict[str, str]]:
#     """Walk through the docs directory and build the index."""
#     index = []

#     for root, _, files in os.walk(docs_path):
#         for file in files:
#             if not file.endswith(".md"):
#                 continue

#             file_path = os.path.join(root, file)
#             rel_path = os.path.relpath(file_path, docs_path)

#             parts = pathlib.Path(rel_path).parts
#             parts_clean = [clean_name(p) for p in parts]

#             # URL path: join with / and convert underscores to hyphens
#             url = "/" + "/".join(
#                 p.replace("_", "-").rsplit(".", 1)[0] for p in parts
#             )

#             doc_info = {
#                 "name": clean_name(file),
#                 "parts": parts_clean,
#                 "url": f"docs{url}",
#                 # "description": extract_description(file_path),
#                 "description": summarize_markdown_local(file_path),
#             }

#             index.append(doc_info)

#     return index


# # Example usage
# if __name__ == "__main__":
#     import json

#     docs_dir = "docs"
#     index = build_docs_index(docs_dir)
#     print(json.dumps(index, indent=2))
#     print(f"Total documents indexed: {len(index)}")


""""""


# import os
# import pathlib
# import json
# from concurrent.futures import ThreadPoolExecutor, as_completed
# from transformers import pipeline

# # Initialize the fast summarization pipeline globally
# summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# def clean_name(name: str) -> str:
#     return name.replace("_", " ").rsplit(".", 1)[0].strip()

# def summarize_markdown(md_path: str) -> str:
#     with open(md_path, "r", encoding="utf-8") as f:
#         content = f.read()

#     truncated = content[:1024]  # truncate to speed up
#     input_len = len(truncated.split())
#     # Ensure max_length is smaller than input length but at least 1
#     max_len = max(1, min(20, input_len // 2))

#     summary = summarizer(truncated, max_length=max_len, min_length=1, do_sample=False)
#     return summary[0]['summary_text'].strip()

# def process_file(docs_path: str, file: str, root: str) -> dict:
#     file_path = os.path.join(root, file)
#     rel_path = os.path.relpath(file_path, docs_path)
#     parts = pathlib.Path(rel_path).parts
#     parts_clean = [clean_name(p) for p in parts]
#     url = "/" + "/".join(p.replace("_", "-").rsplit(".", 1)[0] for p in parts)

#     description = summarize_markdown(file_path)

#     return {
#         "name": clean_name(file),
#         "parts": parts_clean,
#         "url": f"docs{url}",
#         "description": description,
#     }

# def build_docs_index(docs_path: str, max_workers: int = 4) -> list:
#     files_to_process = []

#     for root, _, files in os.walk(docs_path):
#         for file in files:
#             if file.endswith(".md"):
#                 files_to_process.append((docs_path, file, root))

#     index = []
#     with ThreadPoolExecutor(max_workers=max_workers) as executor:
#         futures = [executor.submit(process_file, *args) for args in files_to_process]
#         for future in as_completed(futures):
#             index.append(future.result())

#     return index

# if __name__ == "__main__":
#     docs_dir = "docs"
#     index = build_docs_index(docs_dir, max_workers=8)  # Adjust max_workers for your CPU/GPU
#     with open("docs_index.json", "w", encoding="utf-8") as f:
#         json.dump(index, f, indent=2, ensure_ascii=False)
#     print(f"Indexed {len(index)} documents. Output written to docs_index.json")


""""""

import os
import pathlib
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

ACRONYMS = {"AI", "API", "HTTP", "HTTPS", "SQL", "JSON", "XML", "CPU", "GPU", "OAuth", "CLI", "URL", "DNS", "IP"}

def smart_title_case(name: str) -> str:
    def fix_word(word: str) -> str:
        if word.upper() in ACRONYMS:
            return word.upper()
        return word.capitalize()

    return " ".join(fix_word(w) for w in name.split())

def clean_name(name: str) -> str:
    # Remove file extension (case insensitive)
    if name.lower().endswith(".md"):
        name = name[:-3]
    # Replace underscores and hyphens with spaces
    name = name.replace("_", " ").replace("-", " ").strip()
    # Apply smart title case with acronym handling
    return smart_title_case(name)

def extractive_summary(text: str, sentence_count: int = 2) -> str:
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)

import re

def clean_markdown(text: str) -> str:
    # Remove fenced code blocks (```...```)
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    # Remove inline code `...`
    text = re.sub(r"`[^`]+`", "", text)
    # Remove markdown headings like #, ## etc
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    # Replace markdown links [text](url) with just text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Remove HTML comments <!-- ... -->
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    # Collapse multiple newlines into one
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    # Strip leading/trailing whitespace
    return text.strip()

def summarize_markdown(md_path: str) -> str:
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    cleaned = clean_markdown(content)
    if len(cleaned.split()) < 30:
        return cleaned

    try:
        summary = extractive_summary(cleaned, sentence_count=1).strip()
        if len(summary) > 150:
            summary = summary[:147].rstrip() + "..."
        return summary
    except Exception as e:
        print(f"Summarization error in {md_path}: {e}")
        return cleaned



def process_file(docs_path: str, file: str, root: str) -> dict:
    file_path = os.path.join(root, file)
    rel_path = os.path.relpath(file_path, docs_path)
    parts = pathlib.Path(rel_path).parts
    parts_clean = [clean_name(p) for p in parts]
    url = "/" + "/".join(p.replace("_", "-").rsplit(".", 1)[0] for p in parts)

    description = summarize_markdown(file_path)

    return {
        "name": clean_name(file),
        "parts": parts_clean,
        "url": f"docs{url}",
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
    with open("docs_index.json", "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    print(f"Indexed {len(index)} documents. Output written to docs_index.json")
