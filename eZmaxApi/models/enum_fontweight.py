# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EnumFontweight(str, Enum):
    """
    The Font Weight
    """

    """
    allowed enum values
    """
    NORMAL = 'Normal'
    BOLD = 'Bold'

    @classmethod
    def from_json(cls, json_str: str) -> EnumFontweight:
        """Create an instance of EnumFontweight from a JSON string"""
        return EnumFontweight(json.loads(json_str))


