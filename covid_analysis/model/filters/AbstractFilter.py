from abc import ABC, abstractmethod


class AbstractFilter(ABC):
    """Abstract class for filtering"""

    @abstractmethod
    def apply_to(self, data):
        """
        Filters data based on concrete behavior

        Parameters
        ----------
        data: The data to filter

        Returns
        -------
        list of CountrySummary
        """
        pass;