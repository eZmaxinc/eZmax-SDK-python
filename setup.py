# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "eZmaxApi"
VERSION = "1.2.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 1.10.5, < 2",
    "aenum"
]

setup(
    name=NAME,
    version=VERSION,
    description="eZmax API Definition (Full)",
    author="API Support department",
    author_email="support-api@ezmax.ca",
    url="https://github.com/eZmaxinc/eZmax-SDK-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "eZmax API Definition (Full)"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT License",
    long_description_content_type='text/markdown',
    long_description="""\
    This API expose all the functionnalities for the eZmax and eZsign applications.
    """,  # noqa: E501
    package_data={"eZmaxApi": ["py.typed"]},
)
