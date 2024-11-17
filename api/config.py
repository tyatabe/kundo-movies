from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="KUNDO-SEARCH",
    environments=True,
    root_path="..",  # TODO: change this to "api" when running in a container(?)
    settings_files=["settings.toml", ".secrets.toml"],
)
