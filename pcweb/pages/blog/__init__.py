from pcweb.route import Route
from .blog import *

blog_routes = [r for r in locals().values() if isinstance(r, Route)]