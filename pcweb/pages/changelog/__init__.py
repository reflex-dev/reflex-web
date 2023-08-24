from pcweb.route import Route
from .changelog import *

changelog_routes = [r for r in locals().values() if isinstance(r, Route)]
