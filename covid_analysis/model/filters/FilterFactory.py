import string
from functools import partial

from covid_analysis.model.filters import FilterByName, FilterByThreshold, ComposedFilter


class FilterFactory(object):
    """
    constructs various filter types, using constructor methods
    """

    @classmethod
    def byName(cls, name: string) -> FilterByName:
        return FilterByName(country_name=name)

    @classmethod
    def byLowerBound(cls, field: string, threshold: float) -> FilterByThreshold:
        return FilterByThreshold(field=field, threshold=threshold)

    @classmethod
    def byUpperBound(cls, field: string, threshold: float) -> FilterByThreshold:
        return FilterByThreshold(field=field, threshold=threshold, reversed=True)

    @classmethod
    def byRange(cls, field: string, lower_bound: float, upper_bound: float) -> ComposedFilter:
        return cls.compose(
            cls.byLowerBound(field, lower_bound),
            cls.byUpperBound(field, upper_bound),
        )

    @classmethod
    def compose(cls, *args):
        return ComposedFilter(args)