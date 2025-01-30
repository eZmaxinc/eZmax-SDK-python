# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.2
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class FieldEEzsignformfieldgroupSignerrequirement(str, Enum):
    """
    The Signer requirement of the Ezsignformfieldgroup. **All** means anyone can fill it, **One** means a specific person must fill it.
    """

    """
    allowed enum values
    """
    ALL = 'All'
    ONE = 'One'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FieldEEzsignformfieldgroupSignerrequirement from a JSON string"""
        return cls(json.loads(json_str))


