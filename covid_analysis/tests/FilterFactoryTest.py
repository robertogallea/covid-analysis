import unittest

from covid_analysis.model.filters import FilterByName, FilterFactory, FilterByThreshold, ComposedFilter


class FilterFactoryTest(unittest.TestCase):
    def test_it_creates_name_filters(self):
        self.assertIsInstance(FilterFactory.byName("x"), FilterByName)

    def test_it_creates_lower_bound_filters(self):
        self.assertIsInstance(FilterFactory.byLowerBound("a_field", 1000), FilterByThreshold)

    def test_it_creates_upper_bound_filters(self):
        self.assertIsInstance(FilterFactory.byUpperBound("a_field", 1000), FilterByThreshold)

    def test_it_creates_composed_filters(self):
        self.assertIsInstance(FilterFactory.compose(
            FilterFactory.byUpperBound("a_field", 1000),
            FilterFactory.byLowerBound("a_field", 100),
        ), ComposedFilter)

    def test_it_creates_range_fiter(self):
        self.assertIsInstance(FilterFactory.byRange("a field", 10, 100), ComposedFilter)


if __name__ == '__main__':
    unittest.main()
