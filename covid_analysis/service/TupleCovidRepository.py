import random
import string

from covid_analysis.model import CountrySummary
from covid_analysis.service.CovidRepositoryInterface import CovidRepositoryInterface


class TupleCovidRepository(CovidRepositoryInterface):
    """Tuple-based repository class for COVID data Country Summaries, used mainly for test purpose"""

    def __init__(self, data):
        self.data = data

    def load(self):
        """
        loads data from the repository

        Returns
        -------
        list of CountrySummary
        """
        return self.data