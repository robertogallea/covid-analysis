import json
from collections import namedtuple
from datetime import datetime, timedelta

import requests

from covid_analysis.model.CountrySummary import CountrySummary
from covid_analysis.service.CovidRepositoryInterface import CovidRepositoryInterface
from covid_analysis.utils.CacheObject import cache


class ApiCovidRepository(CovidRepositoryInterface):
    """API-based repository class for COVID data Country Summaries"""

    def __init__(self, baseurl):
        self.base_url = baseurl

    @cache(key="covid_data", expires_after=timedelta(minutes=1))
    def load(self):
        """
        loads data from the repository

        Returns
        -------
        list of CountrySummary
        """
        country_summaries_list = ()
        response = requests.get(self.base_url)

        json_countries = json.loads(response.content)

        for json_country in json_countries["Countries"]:
            country_summary = CountrySummary()
            country_summary.name = json_country[CountryFields.Country]
            country_summary.new_confirmed = json_country[CountryFields.NewConfirmed]
            country_summary.total_confirmed = json_country[CountryFields.TotalConfirmed]
            country_summary.new_deaths = json_country[CountryFields.NewDeaths]
            country_summary.total_deaths = json_country[CountryFields.TotalDeaths]
            country_summary.new_recovered = json_country[CountryFields.NewRecovered]
            country_summary.total_recovered = json_country[CountryFields.TotalRecovered]
            country_summaries_list += (country_summary,)

        return country_summaries_list


CountryFields = namedtuple(
    "CountryFields",
    "Country NewConfirmed TotalConfirmed NewDeaths TotalDeaths NewRecovered TotalRecovered",
    defaults=(
        "Country",
        "NewConfirmed",
        "TotalConfirmed",
        "NewDeaths",
        "TotalDeaths",
        "NewRecovered",
        "TotalRecovered",
    ),
)()
