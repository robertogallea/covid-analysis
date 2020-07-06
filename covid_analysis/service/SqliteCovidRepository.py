import os
import sqlite3

from covid_analysis.model import CountrySummary


class SqliteCovidRepository(object):
    """Sqlite-based repository class for COVID data Country Summaries"""

    table_name = "country_summary"

    def __init__(self, filename):
        self.filename = filename

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

        con = sqlite3.connect(self.filename)
        cursor = con.cursor()

        self.__recreateTable(cursor)

        data = list(map(lambda x: tuple(x.to_dict().values()), country_summaries))

        query = f"""
            INSERT INTO {self.table_name}
                (name, new_deaths, total_deaths, new_confirmed, total_confirmed, new_recovered, total_recovered) 
                VALUES (?,?,?,?,?,?,?)
        """

        cursor.executemany(query, data)
        con.commit()
        cursor.close()
        con.close()

    def load(self):
        """
        loads data from the repository

        Returns
        -------
        list of CountrySummary
        """
        con = sqlite3.connect(self.filename)
        cursor = con.cursor()

        query = f"SELECT * from {self.table_name}"

        country_summaries = []

        for row in cursor.execute(query):
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

    def __recreateTable(self, cursor):
        query = f"DROP TABLE IF EXISTS {self.table_name}"
        cursor.execute(query)

        query = f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                name text PRIMARY KEY,
                new_confirmed text,
                total_confirmed text,
                new_deaths text,
                total_deaths text,
                new_recovered text,
                total_recovered text
            )
        """
        cursor.execute(query)
