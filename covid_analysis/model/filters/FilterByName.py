from covid_analysis.model.filters.AbstractFilter import AbstractFilter


class FilterByName(AbstractFilter):
    """Filter data searching for a given name"""


    def __init__(self, *, country_name):
        """
        Parameters
        ----------
        country_name: the name to search for
        """
        self.__country = country_name

    def apply_to(self, data):
        """
        Parameters
        ----------
        data: The data to filter

        Returns
        -------
        list of CountrySummary
        """
        filtered_data = list(filter(lambda el: el.name.count(self.__country) > 0, data))

        return filtered_data