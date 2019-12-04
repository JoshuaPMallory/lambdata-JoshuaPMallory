"""
Docstring

How to set up a python package


Upload to testpypi.org:
 Add
  python setup.py sdist bdist_wheel
 Remove
  rm dist

Push to testpypi.org
 twine upload --repository-url https://test.pypi.org/legacy/ dist/*
"""

import lambdata_joshuapmallory.plotting_functions
import lambdata_joshuapmallory.utility_functions

class thing:
    """
    This is a docstring
    """

    def __init__(self):
        variable = 1

    def some_function(x):
        print(x)

# import autopep8
# autopep8 --in-place __init__.py