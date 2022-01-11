from piccolo.conf.apps import AppConfig, table_finder

APP_CONFIG = AppConfig(
    app_name="blog",
    migrations_folder_path="app.migrations",
    table_classes=table_finder(modules=["blog.tables"]),
    migration_dependencies=[],
    commands=[],
)
