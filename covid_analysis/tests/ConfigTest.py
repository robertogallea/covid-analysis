import os
import unittest

from covid_analysis.model import Config


class MyTestCase(unittest.TestCase):
    def test_it_has_a_single_instance(self):
        config = Config.get_instance()
        config2 = Config.get_instance()

        self.assertIs(config, config2)

    def test_it_can_read_config_from_file(self):
        content = """
            {
                "a": "b",
                "b": {"c": "d"}
            }
        """
        f = open("test_config.env", "w+")
        f.write(content)
        f.close()

        config = Config()
        config.load("test_config.env")

        self.assertEqual("b", config.a)
        self.assertEqual("d", config.b.c)
        os.remove("test_config.env")


if __name__ == "__main__":
    unittest.main()
