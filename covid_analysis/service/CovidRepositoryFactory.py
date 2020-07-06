class CovidRepositoryFactory:
    """Creates a repository according to the required type"""

    def __init__(self):
        self._repositories = {}
        self._parameters = {}

    def register(self, type, creator, parameters):
        """
        registers a new repository

        Parameters
        ----------
        type: key for the repository
        creator: repository class

        Returns
        -------
        None
        """

        self._repositories[type] = creator
        self._parameters[type] = parameters

    def __call__(self, type):
        """
        factory method for creating repositories

        Parameters
        ----------
        type: requested repository type

        Returns
        -------
        Repository instance

        Raises
        ------
        ValueError if repository is unknown
        """
        repository = self._repositories.get(type)
        if not repository:
            raise ValueError(format)
        return repository(**self._parameters[type]._asdict())
