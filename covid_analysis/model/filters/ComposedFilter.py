from covid_analysis.model.filters import AbstractFilter


class ComposedFilter(AbstractFilter):
    def __init__(self, base_filters):
        """
        Parameters
        ----------
        base_filters: the list of filters
        """
        self._base_filters = base_filters

    def apply_to(self, data):
        """
        Parameters
        ----------
        data: The data to filter

        Returns
        -------
        list of CountrySummary
        """
        filtered_data = data

        for filter in self._base_filters:
            filtered_data = filter.apply_to(filtered_data)

        return filtered_data