from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="KUNDO-SEARCH",
    environments=True,
    root_path="api",
    settings_files=["settings.toml", ".secrets.toml"],
)
