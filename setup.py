"""
lambdata - a collection of data science helper functions for lambda school
"""
import setuptools

REQUIRED = ['unittest'
           ,'numpy'
           ,'pandas'
           ,'autopep8'
           ,'matplotlib'
           ]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION                               = fh.read()
    setuptools.setup(name                          = "lambdata-JoshuaPMallory"
                    ,version                       = "0.1.4"
                    ,author                        = "JoshuaPMallory"
                    ,description                   = "a collection of data science helper functions"
                    ,long_description              = LONG_DESCRIPTION
                    ,long_description_content_type = "text/markdown"
                    ,url                           = "https://lambdaschool.com/courses/data-science"
                    ,packages                      = setuptools.find_packages()
                    ,python_requires               = ">=3.5"
                    ,install_requires              = REQUIRED
                    ,classifiers                   = ["Programming Language :: Python :: 3"
                                                     ,"Operating System :: OS Independent"
                                                     ,"License :: OSI Approved :: Apache License 2.0"
                                                     ]
    )


