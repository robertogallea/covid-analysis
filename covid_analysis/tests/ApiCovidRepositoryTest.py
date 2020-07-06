import unittest

from covid_analysis.model import CountrySummary
from covid_analysis.service import ApiCovidRepository


class CovidApiRepositoryTest(unittest.TestCase):
    def test_it_loads_a_tuple_of_countries(self):
        baseurl = "https://api.covid19api.com/summary"
        repo = ApiCovidRepository(baseurl)
        countries = repo.load()

        self.assertIsInstance(countries, tuple)

        for country_summary in countries:
            self.assertIsInstance(country_summary, CountrySummary)


if __name__ == "__main__":
    unittest.main()
