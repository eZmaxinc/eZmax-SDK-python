# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class EnumTextvalidation(str, Enum):
    """
    The text validation
    """

    """
    allowed enum values
    """
    NONE = 'None'
    DATE_LEFT_PARENTHESIS_YYYY_MINUS_MM_MINUS_DD_RIGHT_PARENTHESIS = 'Date (YYYY-MM-DD)'
    DATE_LEFT_PARENTHESIS_MM_SLASH_DD_SLASH_YYYY_RIGHT_PARENTHESIS = 'Date (MM/DD/YYYY)'
    DATE_LEFT_PARENTHESIS_MM_SLASH_DD_SLASH_YY_RIGHT_PARENTHESIS = 'Date (MM/DD/YY)'
    DATE_LEFT_PARENTHESIS_DD_SLASH_MM_SLASH_YYYY_RIGHT_PARENTHESIS = 'Date (DD/MM/YYYY)'
    DATE_LEFT_PARENTHESIS_DD_SLASH_MM_SLASH_YY_RIGHT_PARENTHESIS = 'Date (DD/MM/YY)'
    EMAIL = 'Email'
    LETTERS = 'Letters'
    NUMBERS = 'Numbers'
    ZIP = 'Zip'
    ZIP_PLUS_4 = 'Zip+4'
    POSTALCODE = 'PostalCode'
    CUSTOM = 'Custom'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EnumTextvalidation from a JSON string"""
        return cls(json.loads(json_str))


