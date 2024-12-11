
"""
Module to expose more detailed version info for the installed `numpy`
"""
version = "2.2.0"
__version__ = version
full_version = version

git_revision = "e7a123b2d3eca9897843791dd698c1803d9a39c2"
release = 'dev' not in version and '+' not in version
short_version = version.split("+")[0]
