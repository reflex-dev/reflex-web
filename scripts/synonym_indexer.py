""" Dynamically generate synonyms for docs to better type match"""
import os
import pathlib
import typesense

from typesense_indexer import TYPESENSE_CONFIG

client = typesense.Client(TYPESENSE_CONFIG)

def get_folder_hierarchy(root: str) -> dict:
    """Recursively build folder hierarchy from root, ignoring unwanted folders."""
    hierarchy = {}
    for entry in os.scandir(root):
        if entry.is_dir() and entry.name not in ("__pycache__", ".git", ".venv"):
            hierarchy[entry.name] = get_folder_hierarchy(entry.path)
    return hierarchy

def generate_synonyms(name: str) -> list[str]:
    """
    Generate multiple synonym forms for a folder/component name:
    - flattened lowercase: reactflow
    - lowercase spaced: react flow
    - title case spaced: React Flow
    - underscore: react_flow
    - hyphen: react-flow
    - camelcase: ReactFlow
    """
    clean_name = name.replace("_", " ").replace("-", " ").strip()
    words = clean_name.split()

    synonyms = set()

    # 1) Flattened lowercase
    synonyms.add("".join(w.lower() for w in words))
    # 2) Lowercase spaced
    synonyms.add(" ".join(w.lower() for w in words))
    # 3) Title case spaced
    synonyms.add(" ".join(w.capitalize() for w in words))
    # 4) Original underscore
    synonyms.add("_".join(w.lower() for w in words))
    # 5) Original hyphen
    synonyms.add("-".join(w.lower() for w in words))
    # 6) CamelCase
    synonyms.add("".join(w.capitalize() for w in words))

    return list(synonyms)

def flatten_hierarchy(hierarchy: dict) -> dict:
    """
    Flatten nested folder hierarchy into a single dict with synonyms
    keyed by flattened lowercase name.
    """
    flat = {}

    def recurse(subtree):
        for key, value in subtree.items():
            # Flatten key for canonical form
            key_flat = "".join(key.lower().split("_")).replace("-", "")
            flat[key_flat] = {"synonyms": generate_synonyms(key)}
            if value:
                recurse(value)

    recurse(hierarchy)
    return flat

def main() -> bool:
    try:
        docs_root = pathlib.Path("docs")
        hierarchy = get_folder_hierarchy(docs_root)
        SYNONYMS = flatten_hierarchy(hierarchy)

        print("Upserting new synonyms to Typesense ...")
        for canonical, info in SYNONYMS.items():
            client.collections["docs"].synonyms.upsert(
                canonical,
                {"synonyms": info["synonyms"]}
            )

        print("Synonyms synced successfully!")
        return True

    except Exception as e:
        print("Error syncing synonyms:", e)
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
