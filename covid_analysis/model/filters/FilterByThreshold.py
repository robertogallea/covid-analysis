from covid_analysis.model.filters.AbstractFilter import AbstractFilter


class FilterByThreshold(AbstractFilter):
    """Filter data using threshold value for a given field"""

    def __init__(self, *, field, threshold, reversed=False):
        """
        Parameters
        ----------
        field: the field used for thresholding
        threshold: the threshold value
        reversed: if True, threshold is used as upperbound, default: False
        """
        self.__threshold = threshold
        self.__field = field
        self.__reversed = reversed


    def apply_to(self, data):
        """
        Parameters
        ----------
        data: The data to filter

        Returns
        -------
        list of CountrySummary
        """
        method = self.__get_smaller_than if self.__reversed else self.__get_greater_than

        filtered_data = list(
            filter(
                method,
                data
            )
        )

        return filtered_data

    def __get_greater_than(self, el):
        attribute = self.__get_attribute(el)

        return attribute >= self.__threshold

    def __get_smaller_than(self, el):
        attribute = self.__get_attribute(el)

        return attribute <= self.__threshold

    def __get_attribute(self, el):
        return getattr(el, self.__field)