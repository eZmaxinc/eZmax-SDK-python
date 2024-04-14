# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.1
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class FieldEEzsigntemplateglobalModule(str, Enum):
    """
    The Module for the Ezsigntemplateglobal
    """

    """
    allowed enum values
    """
    ALL = 'All'
    INSCRIPTION = 'Inscription'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FieldEEzsigntemplateglobalModule from a JSON string"""
        return cls(json.loads(json_str))

