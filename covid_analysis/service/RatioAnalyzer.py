import matplotlib.pyplot as plt
from datetime import datetime
from mpl_toolkits import mplot3d

from covid_analysis.service import CovidRepositoryInterface


class RatioAnalyzer(object):
    """Service for analyzing country summaries data ratios"""

    def __init__(self, repo: CovidRepositoryInterface):
        """
        Parameters
        ----------
        repo: the repository used to retrieve data to analyze
        """
        self.country_summaries = repo.load()

    def plot_ratio_histogram(self):
        confirmed_ratios = list(self.get_new_confirmed_ratio())
        recovered_ratios = list(self.get_new_recovered_ratio())
        deaths_ratios = list(self.get_new_deaths_ratio())

        n, bins, patches = plt.hist(
            x=[confirmed_ratios, recovered_ratios, deaths_ratios],
            bins=10,
            color=["#ea4335", "#4285f4", "#333333"],
            alpha=1,
            rwidth=0.85,
            range=(0, 1),
            label=["Confirmed ratio", "Recovered ratio", "Deaths ratio"],
        )


        plt.legend()
        plt.grid(axis="y", alpha=0.75)
        plt.xlabel("Daily / Total ratio")
        plt.ylabel("Frequency")
        plt.title("Daily impact of virus")
        plt.show()

    def get_new_confirmed_ratio(self):
        """
        Returns
        -------
        ratio of daily confirmed infected over total confirmed infected
        """
        return map(
            lambda country_summary: self._compute_ratio(
                country_summary.new_confirmed, country_summary.total_confirmed
            ),
            self.country_summaries,
        )

    def get_new_recovered_ratio(self):
        """
        Returns
        -------
        ratio of daily confirmed recovered over total confirmed recovered
        """
        return map(
            lambda country_summary: self._compute_ratio(
                country_summary.new_recovered, country_summary.total_recovered
            ),
            self.country_summaries,
        )

    def get_new_deaths_ratio(self):
        """
        Returns
        -------
        ratio of daily confirmed deaths over total confirmed deaths
        """
        return map(
            lambda country_summary: self._compute_ratio(
                country_summary.new_deaths, country_summary.total_deaths
            ),
            self.country_summaries,
        )

    def _compute_ratio(self, new, total):
        try:
            ratio = new / (total - new)
        except ZeroDivisionError:
            ratio = 0

        return ratio

    def __call__(self, *args, **kwargs):
        """
        factory method for generating dynamic datasets.

        Examples:
            analyzer = CountrySummariesAnalyzer(country_summaries)
            analyzer(new_confirmed_ratio=False, new_recovered_ratio=True, new_deaths_ratio=True))

        Parameters
        ----------
        kwargs: new_confirmed_ratio | new_recovered_ratio | new_deaths_ratio, boolean

        Returns
        -------
        a dict with the required ratios where keys are country names, values are dicts with required ratio values
        e.g.
        {
          "Italy": {
            "new_confirmed_ratio": 0.023235,
            "new_recovered_ratio": 0.185787,
            "new_deaths_ratio": 0.005477
          }
          ...
        }
        """
        ratios = {
            "new_confirmed_ratio": list(self.get_new_confirmed_ratio())
            if "new_confirmed_ratio" in kwargs.keys()
            else [0,] * len(self.country_summaries),
            "new_recovered_ratio": list(self.get_new_recovered_ratio())
            if "new_recovered_ratio" in kwargs.keys()
            else [0,] * len(self.country_summaries),
            "new_deaths_ratio": list(self.get_new_deaths_ratio())
            if "new_deaths_ratio" in kwargs.keys()
            else [0,] * len(self.country_summaries),
        }

        countries = list(map(lambda country: country.name, self.country_summaries))

        return {
            key: dict(args)
            for key, *args in zip(
                *iter(
                    [
                        countries,
                        *map(
                            lambda x: list(zip([x[0],] * len(x[1]), x[1])),
                            filter(
                                lambda x: x[0] in kwargs.keys()
                                and kwargs[x[0]] is True,
                                ratios.items(),
                            ),
                        ),
                    ]
                )
            )
        }

    def cluster_countries(self, *args, num_cluster=3, draw_plot=False, save_to=None):
        """
        clusterizes data and plot clusters

        Parameters:
        -----------------
        num_cluster: the number of cluster to discover

        Returns:
        -----------------
        a nested dict containing cluster centroids and clustered data
        """

        ratios_confirmed = list(self.get_new_confirmed_ratio())
        ratios_recovered = list(self.get_new_recovered_ratio())
        ratios_deaths = list(self.get_new_deaths_ratio())
        names = list(map(lambda x: x.name, self.country_summaries))

        ratios_values = list(zip(ratios_confirmed, ratios_recovered, ratios_deaths))

        # clustering
        from sklearn.cluster import KMeans
        import numpy as np

        X = np.array(ratios_values)
        kmeans = KMeans(n_clusters=num_cluster, random_state=0).fit(X)

        labeled_names = list(
            zip(
                names, kmeans.labels_, ratios_confirmed, ratios_recovered, ratios_deaths
            )
        )
        zones = [
            list(filter(lambda x: x[1] == i, labeled_names))
            for i in range(0, num_cluster)
        ]

        if draw_plot:
            self._draw_clusters_plot(kmeans, zones)

        if save_to:
            self._save_results(zones, save_to)

        return {"centers": kmeans.cluster_centers_, "data": zones}

    def _draw_clusters_plot(self, kmeans, zones):
        """
        display clustered data

        Parameters
        ----------
        kmeans: the cluster info
        zones: the cluster data

        Returns
        -------
        None
        """
        colors = ("r", "g", "b", "c", "m", "y")

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        for i in range(0, len(zones)):
            ax.scatter3D(
                list(map(lambda x: x[2], zones[i])),
                list(map(lambda x: x[3], zones[i])),
                list(map(lambda x: x[4], zones[i])),
                c=colors[i],
                marker=".",
            )
        for i in range(0, len(zones)):
            ax.scatter3D(
                kmeans.cluster_centers_[i][0],
                kmeans.cluster_centers_[i][1],
                kmeans.cluster_centers_[i][2],
                c=colors[i],
                marker="o",
                edgecolors="black",
            )

        ax.set_xlabel("New confirmed ratio")
        ax.set_ylabel("New recovered ratio")
        ax.set_zlabel("New deaths ratio")
        plt.show()

    def _save_results(self, zones, save_to):
        """
        Saves data to text file

        Parameters
        ----------
        zones: data to save
        save_to: destination filename

        Returns
        -------
        None
        """
        with open(save_to, "a") as f:
            f.write(f"Analisi del {datetime.now().strftime('%d-%m-%Y - %H:%M:%S')}\n\n")
            for i in zones:
                f.write(f"Nazioni in zona {i[0][1]}\n")
                f.write("\n".join(map(lambda x: "- " + x[0], i)))
                f.write("\n\n")
