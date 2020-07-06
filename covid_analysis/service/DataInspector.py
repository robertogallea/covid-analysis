import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

from covid_analysis.model.filters import AbstractFilter
from covid_analysis.service import CovidRepositoryInterface



class DataInspector(object):
    """class for various graphic data representation"""

    def __init__(self, repo: CovidRepositoryInterface, filter: AbstractFilter = None) -> object:
        """Initialization

        :param repo: the repository used to retrieve the data for the plots
        """
        super().__init__()

        rawdata = repo.load()

        if (filter is not None):
            rawdata = filter.apply_to(rawdata)

        self.data = pd.DataFrame.from_records([r.to_dict() for r in rawdata])


    def heat_map(self, save_figure_to=None):
        """heat map of data columns correlation"""
        sns.set(style="ticks")
        corr = self.data.corr()
        g = sns.heatmap(
            corr,
            vmax=1,
            vmin=0.5,
            square=True,
            linewidths=0.5,
            cbar_kws={"shrink": 0.5},
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
        )
        sns.despine()
        g.figure.set_size_inches(14, 10)

        plt.show()

        if save_figure_to:
            self._saveFigure(g.figure, save_figure_to)

    def pairplot(self, save_figure_to=None):
        """pairplots of data columns"""
        g = sns.pairplot(self.data)
        plt.show()

        if save_figure_to:
            self._saveFigure(g, save_figure_to)

    def swarmplot(self, *args, about, save_figure_to=None):
        """
        swarmplot of particolar column

        Parameters
        ----------
        about: dataset column of interest

        Returns
        -------
        None
        """
        try:
            mean = self.data[about].mean()
        except KeyError:
            print(f"The '{about}' key does not exist in this dataset")
        else:
            plot_data = self.data[self.data[about] > mean].reset_index(drop=True)

            max_value = plot_data[about].max()
            max_country = plot_data[plot_data[about] == max_value]["name"].values[0]
            max_index = plot_data[plot_data[about] == max_value]["name"].index[0]

            min_value = plot_data[about].min()
            min_country = plot_data[plot_data[about] == min_value]["name"].values[0]
            min_index = plot_data[plot_data[about] == min_value]["name"].index[0]

            g = sns.swarmplot(y="name", x=about, data=plot_data, size=7)

            self._annotate_plot("max", max_country, max_index, max_value, about)
            self._annotate_plot("min", min_country, min_index, min_value, about)

            g.figure.set_size_inches(12, 8)
            plt.show()

            if save_figure_to:
                self._saveFigure(g.figure, save_figure_to)

    def _annotate_plot(self, metric, country, index, value, show):
        plt.annotate(
            s=f"{metric} {show}: {country}",
            xy=(value, index),
            xytext=(value * 0.5, index + 2),
            arrowprops={"facecolor": "gray", "width": 5, "shrink": 0.03},
            backgroundcolor="white",
        )

    @classmethod
    def _saveFigure(cls, g, save_figure_to):
        """ saves figure to file, if path does not exist, creates it """
        try:
            dir = os.path.dirname(save_figure_to)

            if not os.path.exists(dir):
                os.makedirs(dir)

            g.savefig(save_figure_to)
        except IOError:
            print(f"Unable to write to file {save_figure_to}")

