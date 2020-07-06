import json
from collections import namedtuple


class Config:
    """
    Converts a json csv file into a python object
    Example:
        {
            a: "123",
            b: {
                c: "ok"
            }
        }

    Config().get_instance().a is equal to "123"
    Config().get_instance().b.c is equal to "ok"
    """

    __instance = None
    __config = {}

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Config.__instance == None:
            Config()
        return Config.__instance

    def __init__(self):
        """
        Virtually private constructor.

        Raises
        ------
        Exception, if class has been already instantiated
        """
        if Config.__instance != None:
            raise Exception("This class is a singleton!")

        Config.__instance = self

    def load(self, filename):
        """
        Loads the filename

        Parameters
        ----------
        arg filename the location of the configuration file

        Returns
        -------
        Config
        """
        f = open(filename)
        content = f.read()
        self.__config = json.loads(
            content, object_hook=lambda d: namedtuple("config", d.keys())(*d.values())
        )
        f.close()
        return self

    def __getattr__(self, item):
        """
        Delegates attribute resolution to __config internal object

        Parameters
        ----------
        item: name of the required attributesud

        Returns
        -------
        the value of the attribute
        """
        return getattr(self.__config, item)
