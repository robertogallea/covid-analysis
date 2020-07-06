import unittest

from covid_analysis.model.filters import FilterByName, FilterByThreshold
from covid_analysis.model import CountrySummary


class CountrySummaryFiltersTest(unittest.TestCase):
    def test_it_can_return_filter_by_name_portion(self):
        first_country_summary = CountrySummary()
        first_country_summary.name = "Italy"
        second_country_summary = CountrySummary()
        second_country_summary.name = "U.S.A."

        country_summaries = (first_country_summary, second_country_summary)

        filter = FilterByName(country_name="Italy")

        filtered_summaries = filter.apply_to(country_summaries)

        self.assertEqual(1, len(filtered_summaries))
        self.assertIs(first_country_summary, filtered_summaries[0])

    def test_it_can_return_filter_by_new_confirmed_threshold(self):
        first_country_summary = CountrySummary()
        first_country_summary.new_confirmed = 10
        first_country_summary.total_recovered = 1
        second_country_summary = CountrySummary()
        second_country_summary.new_confirmed = 9
        second_country_summary.total_recovered = 2

        country_summaries = (first_country_summary, second_country_summary)

        filter_new_confirmed = FilterByThreshold(field="new_confirmed", threshold=10)

        filtered_summaries = filter_new_confirmed.apply_to(country_summaries)

        self.assertEqual(1, len(filtered_summaries))
        self.assertIs(first_country_summary, filtered_summaries[0])

        filter_total_recovered = FilterByThreshold(field="total_recovered", threshold=2)

        filtered_summaries = filter_total_recovered.apply_to(country_summaries)

        self.assertEqual(1, len(filtered_summaries))
        self.assertIs(second_country_summary, filtered_summaries[0])

    def test_it_can_return_filter_by_new_confirmed_threshold_reversed(self):
        first_country_summary = CountrySummary()
        first_country_summary.new_confirmed = 10
        first_country_summary.total_recovered = 1
        second_country_summary = CountrySummary()
        second_country_summary.new_confirmed = 9
        second_country_summary.total_recovered = 2

        country_summaries = (first_country_summary, second_country_summary)

        filter_new_confirmed = FilterByThreshold(
            field="new_confirmed", threshold=9, reversed=True
        )

        filtered_summaries = filter_new_confirmed.apply_to(country_summaries)

        self.assertEqual(1, len(filtered_summaries))
        self.assertIs(second_country_summary, filtered_summaries[0])

        filter_total_recovered = FilterByThreshold(
            field="total_recovered", threshold=1, reversed=True
        )

        filtered_summaries = filter_total_recovered.apply_to(country_summaries)

        self.assertEqual(1, len(filtered_summaries))
        self.assertIs(first_country_summary, filtered_summaries[0])


if __name__ == "__main__":
    unittest.main()
