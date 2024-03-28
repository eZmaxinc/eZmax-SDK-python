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
from enum import Enum
from typing_extensions import Self


class FieldEEzsignannotationType(str, Enum):
    """
    The type of the Ezsignannotation.  1. **StrikethroughBlock** is a box with hatching. 2. **StrikethroughLine** is a red line to cross words. 3. **Text** is a simple Text.
    """

    """
    allowed enum values
    """
    STRIKETHROUGHBLOCK = 'StrikethroughBlock'
    STRIKETHROUGHLINE = 'StrikethroughLine'
    TEXT = 'Text'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FieldEEzsignannotationType from a JSON string"""
        return cls(json.loads(json_str))


