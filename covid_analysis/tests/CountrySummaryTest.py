import os
import unittest

from covid_analysis.model import Config, CountrySummary


class CountrySummaryTest(unittest.TestCase):
    def test_it_can_be_converted_to_flat_dict(self):
        summary = CountrySummary()
        summary.name = "test"
        summary.new_deaths = 100
        summary.total_deaths = 1000
        summary.new_confirmed = 200
        summary.total_confirmed = 2000
        summary.new_recovered = 300
        summary.total_recovered = 3000

        self.assertEqual(
            {
                "name": "test",
                "new_deaths": 100,
                "total_deaths": 1000,
                "new_confirmed": 200,
                "total_confirmed": 2000,
                "new_recovered": 300,
                "total_recovered": 3000,
            },
            summary.to_dict(),
        )

    def test_two_country_summaries_can_be_compared_for_equality(self):
        summary1 = CountrySummary()
        summary1.name = "test"
        summary1.new_deaths = 100
        summary1.total_deaths = 1000
        summary1.new_confirmed = 200
        summary1.total_confirmed = 2000
        summary1.new_recovered = 300
        summary1.total_recovered = 3000

        summary2 = CountrySummary()
        summary2.name = "test"
        summary2.new_deaths = 100
        summary2.total_deaths = 1000
        summary2.new_confirmed = 200
        summary2.total_confirmed = 2000
        summary2.new_recovered = 300
        summary2.total_recovered = 3000

        self.assertEqual(summary1, summary2)
