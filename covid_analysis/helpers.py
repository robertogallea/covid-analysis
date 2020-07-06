from covid_analysis.service import CovidRepositoryFactory
import importlib


def create_repository_factory(config):
    """
    Creates CountryRepositoryFactory and register all available repositories

    Parameters
    ----------
    config: main configuration object

    Returns
    -------
    CovidRepositoryFactory
    """
    covid_repository_factory = CovidRepositoryFactory()

    for key, repository_name in config.available_repository_types._asdict().items():
        repository_class = getattr(
            importlib.import_module("covid_analysis.service." + repository_name),
            repository_name,
        )
        parameters = getattr(config, key)

        covid_repository_factory.register(key, repository_class, parameters)

    return covid_repository_factory
