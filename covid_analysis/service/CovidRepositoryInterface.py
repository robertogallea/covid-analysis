from abc import ABCMeta, abstractmethod


class CovidRepositoryInterface(metaclass=ABCMeta):
    """Abstract repository class for COVID data Country Summaries"""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load') and
                callable(subclass.load))

    @abstractmethod
    def load(self):
        """
        loads data from the repository

        Returns
        -------
        list of CountrySummary
        """
        pass
