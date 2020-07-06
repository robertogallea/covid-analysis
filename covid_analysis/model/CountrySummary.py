from dataclasses import dataclass


@dataclass
class CountrySummary(object):
    """Dataclass Object representing a country summary"""

    name: str = None
    new_confirmed: int = 0
    total_confirmed: int = 0
    new_recovered: int = 0
    total_recovered: int = 0
    new_deaths: int = 0
    total_deaths: int = 0

    def to_dict(self):
        return {
            "name": self.name,
            "new_deaths": self.new_deaths,
            "total_deaths": self.total_deaths,
            "new_confirmed": self.new_confirmed,
            "total_confirmed": self.total_confirmed,
            "new_recovered": self.new_recovered,
            "total_recovered": self.total_recovered,
        }

