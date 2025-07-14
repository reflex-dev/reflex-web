# component_discovery.py
import logging
from pathlib import Path

logger = logging.getLogger(__name__)
_component_names = None

def get_component_names() -> list[str]:
    """Scan docs/library for .md files and return clean slugs (no -ll suffix)."""
    global _component_names
    if _component_names is not None:
        return _component_names

    repo_root = Path(__file__).parent
    library_root = repo_root / 'docs' / 'library'
    names = set()

    if library_root.exists():
        for md in library_root.rglob('*.md'):
            slug = md.stem
            # strip “-ll”
            if slug.endswith('-ll'):
                slug = slug[:-3]
            # variants: hyphens, underscores, plain
            names.add(slug)
            names.add(slug.replace('-', '_'))
            names.add(slug.replace('_', ''))
    else:
        logger.warning(f"docs/library not found at {library_root}")

    _component_names = sorted(names)
    logger.info(f"Discovered {len(_component_names)} components")
    return _component_names
