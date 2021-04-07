import fire
from DocUtilities import *


@doc(main_docstring())
class Calculator(object):

    def double(self, number):
        return 2 * number

    def half(self, number):
        """ANother one"""
        return number / 2


if __name__ == '__main__':
    fire.Fire(Calculator)
