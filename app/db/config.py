from piccolo.conf.apps import AppRegistry

from .engine import get_database_engine
from app.core.config import settings

DB = get_database_engine(settings.DATABASE_DSN)

APP_REGISTRY = AppRegistry(
    apps=["app"]
)
