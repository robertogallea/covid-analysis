import csv

from covid_analysis.model.CountrySummary import CountrySummary
from covid_analysis.service.CovidRepositoryInterface import CovidRepositoryInterface


class StorageCovidRepository(CovidRepositoryInterface):
    """Storage-based repository class for COVID data Country Summaries"""

    def __init__(self, filename):
        self.filename = filename

    def load(self):
        """
        loads data from the repository

        Returns
        -------
        list of CountrySummary
        """
        country_summaries = ()

        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter="|")

            for row in csv_reader:
                country_summary = CountrySummary()
                country_summary.name = row[0]
                country_summary.new_confirmed = int(row[1])
                country_summary.total_confirmed = int(row[2])
                country_summary.new_deaths = int(row[3])
                country_summary.total_deaths = int(row[4])
                country_summary.new_recovered = int(row[5])
                country_summary.total_recovered = int(row[6])
                country_summaries += (country_summary,)

        return country_summaries

    def save(self, country_summaries):
        """
        saves data to storage

        Parameters
        ----------
        country_summaries: the data to save
        filename: destination file

        Returns
        None
        """

        csv = ""
        for user in country_summaries:
            csv += (
                user.name
                + "|"
                + str(user.new_confirmed)
                + "|"
                + str(user.total_confirmed)
                + "|"
                + str(user.new_deaths)
                + "|"
                + str(user.total_deaths)
                + "|"
                + str(user.new_recovered)
                + "|"
                + str(user.total_recovered)
                + "\n"
            )
        csv = csv[:-1]

        f = open(self.filename, "w+")
        f.write(csv)
        f.close()
