from lib import hello_world

import unittest


class HelloWorldTestSuite(unittest.TestCase):
    """Test Hello World function"""

    def test_hello_world(self):
        hello_world()
        assert True


if __name__ == '__main__':
    unittest.main()