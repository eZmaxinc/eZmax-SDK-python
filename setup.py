"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.48
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "eZmaxApi"
VERSION = "1.0.48"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="eZmax API Definition",
    author="API Support department",
    author_email="support-api@ezmax.ca",
    url="https://github.com/eZmaxinc/eZmax-SDK-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "eZmax API Definition"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT License",
    long_description="""\
    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501
    """
)
