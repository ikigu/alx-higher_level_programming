#!/usr/bin/python3

"""Creates a rebel int class"""


class MyInt(int):
    """Creates rebel int class"""

    def __init__(self, value):
        """Initiates the class"""
        self.value = value

    def __eq__(self, other):
        """Checks equality"""

        if other == self.value:
            return False
        else:
            return True

    def __ne__(self, other):
        """Checks inequality"""

        if other != self.value:
            return False
        else:
            return True
