import random
import string

from covid_analysis.model import CountrySummary
from covid_analysis.service.CovidRepositoryInterface import CovidRepositoryInterface


class DummyCovidRepository(CovidRepositoryInterface):
    """Dummy-data repository class for COVID data Country Summaries, used mainly for test purpose"""

    def load(self):
        """
        loads data from the repository

        Returns
        -------
        list of CountrySummary
        """
        dummy_country_summaries = ()

        for i in range(0, 100):
            country_summary = CountrySummary()
            country_summary.name = self.__randomString(20)
            country_summary.new_confirmed = random.randint(1, 1000)
            country_summary.new_deaths = random.randint(1, 1000)
            country_summary.total_deaths = random.randint(1, 10000) + country_summary.new_deaths
            country_summary.total_confirmed = random.randint(1, 10000) + country_summary.new_confirmed
            country_summary.new_recovered = random.randint(1, 1000)
            country_summary.total_recovered = random.randint(1, 10000) + country_summary.new_recovered

            dummy_country_summaries += (country_summary,)

        return dummy_country_summaries

    def __randomString(self, max_string_length=8):
        letters = string.ascii_lowercase

        return "".join(
            random.choice(letters) for i in range(random.randint(1, max_string_length))
        )
