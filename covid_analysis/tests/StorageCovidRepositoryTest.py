import os
import unittest

from covid_analysis.model import CountrySummary
from covid_analysis.service import StorageCovidRepository


class StorageCovidRepositoryTest(unittest.TestCase):
    def test_it_saves_to_file(self):
        filename = "file.csv"
        first_country = CountrySummary()
        first_country.name = "aa"
        first_country.new_confirmed = 100
        second_country = CountrySummary()
        second_country.name = "bb"
        second_country.new_deaths = 150

        country_summaries = [first_country, second_country]

        repository = StorageCovidRepository(filename=filename)
        repository.save(country_summaries)

        f = open(filename, "r")
        content = f.read()
        f.close()

        self.assertEqual("aa|100|0|0|0|0|0\nbb|0|0|150|0|0|0", content)

    def test_it_loads_from_file(self):
        filename = "file.csv"
        f = open(filename, "w+")
        f.write("aa|100|0|0|0|0|0\nbb|0|0|150|0|0|0")
        f.close()

        repository = StorageCovidRepository(filename=filename)

        country_summaries = repository.load()

        self.assertEqual("aa", country_summaries[0].name)
        self.assertEqual("bb", country_summaries[1].name)

    def tearDown(self) -> None:
        os.remove("file.csv")


if __name__ == "__main__":
    unittest.main()
