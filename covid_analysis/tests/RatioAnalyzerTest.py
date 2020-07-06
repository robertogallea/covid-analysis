import unittest
from collections import namedtuple

from covid_analysis.model import CountrySummary
from covid_analysis.service import DummyCovidRepository, CovidRepositoryFactory, TupleCovidRepository, RatioAnalyzer


class RatioAnalyzerTest(unittest.TestCase):
    def test_it_can_be_fed_with_a_tuple(self):
        repo = DummyCovidRepository()

        analyzer = RatioAnalyzer(repo)
        self.assertIsNotNone(analyzer)


    def test_it_returns_percentage_increase_for_each_country(self):
        country_summary = CountrySummary()
        country_summary.total_confirmed = 110
        country_summary.new_confirmed = 10

        repo = TupleCovidRepository((country_summary,))
        analyzer = RatioAnalyzer(repo)

        self.assertEqual((0.1,), tuple(analyzer.get_new_confirmed_ratio()))

    def test_it_can_call_class_by_passing_which_statistics_should_be_generated(self):
        country_summary = CountrySummary()
        country_summary.name = "Italy"
        country_summary.total_confirmed = 110
        country_summary.new_confirmed = 10
        country_summary.total_recovered = 210
        country_summary.new_recovered = 10
        country_summary.total_deaths = 410
        country_summary.new_deaths = 10

        repo = TupleCovidRepository((country_summary,))
        analyzer = RatioAnalyzer(repo)
        self.assertEqual(
            {
                "Italy": {
                    "new_confirmed_ratio": 0.1,
                    "new_recovered_ratio": 0.05,
                    "new_deaths_ratio": 0.025,
                }
            },
            analyzer(
                new_confirmed_ratio=True,
                new_recovered_ratio=True,
                new_deaths_ratio=True,
            ),
        )

        self.assertEqual(
            {"Italy": {"new_recovered_ratio": 0.05, "new_deaths_ratio": 0.025,}},
            analyzer(
                new_confirmed_ratio=False,
                new_recovered_ratio=True,
                new_deaths_ratio=True,
            ),
        )

        self.assertEqual(
            {"Italy": {"new_recovered_ratio": 0.05,}},
            analyzer(new_recovered_ratio=True, new_deaths_ratio=False),
        )


if __name__ == "__main__":
    unittest.main()
