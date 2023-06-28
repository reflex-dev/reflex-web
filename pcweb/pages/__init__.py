from pcweb.route import Route
from .docs import *
from .blog import *
from .index import index

routes = [r for r in locals().values() if isinstance(r, Route)]
