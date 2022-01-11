from pydantic import HttpUrl, PostgresDsn, validate_arguments

from piccolo.engine.base import Engine
from piccolo.engine.sqlite import SQLiteEngine
from piccolo.engine.postgres import PostgresEngine

@validate_arguments
def get_database_engine(dsn: HttpUrl | PostgresDsn) -> Engine:
    if dsn.startswith("postgres://"):
        return PostgresEngine(config={
            "dsn": dsn
        })

    elif dsn.startswith("sqlite://"):
        return SQLiteEngine(
            path=dsn.replace("sqlite://", "", 1)
        )

    else:
        raise Exception("Unsupported database engine")
