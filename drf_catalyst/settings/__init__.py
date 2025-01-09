from .base import env


if env('DEBUG'):
    from .development import *
else:
    from .production import *
