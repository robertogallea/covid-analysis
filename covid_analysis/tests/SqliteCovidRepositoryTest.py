import os
import unittest

from covid_analysis.model import CountrySummary
from covid_analysis.service import SqliteCovidRepository


class SqliteCovidRepositoryTest(unittest.TestCase):
    dbfilename = "db.sqlite"

    def test_it_creates_db_if_not_exists(self):
        first_country = CountrySummary()
        first_country.name = "aa"
        first_country.new_confirmed = 100
        second_country = CountrySummary()
        second_country.name = "bb"
        second_country.new_deaths = 150

        country_summaries = [first_country, second_country]

        repository = SqliteCovidRepository(filename=self.dbfilename)
        repository.save(country_summaries)

        self.assertTrue(
            os.path.exists(self.dbfilename) and os.path.isfile(self.dbfilename)
        )

    def test_it_saves_to_db(self):
        first_country = CountrySummary()
        first_country.name = "aa"
        first_country.new_confirmed = 100
        second_country = CountrySummary()
        second_country.name = "bb"
        second_country.new_deaths = 150

        country_summaries = [first_country, second_country]

        repository = SqliteCovidRepository(filename=self.dbfilename)
        repository.save(country_summaries)

        loaded_data = repository.load()

        self.assertEqual(loaded_data, country_summaries)

    def tearDown(self) -> None:
        os.remove(self.dbfilename)


if __name__ == "__main__":
    unittest.main()
