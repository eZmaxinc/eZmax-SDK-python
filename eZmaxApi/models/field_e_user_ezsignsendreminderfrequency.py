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


class FieldEUserEzsignsendreminderfrequency(str, Enum):
    """
    Frequency at which reminders will be sent to signers that haven't signed the documents
    """

    """
    allowed enum values
    """
    NONE = 'None'
    DAILY = 'Daily'
    WEEKLY = 'Weekly'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FieldEUserEzsignsendreminderfrequency from a JSON string"""
        return cls(json.loads(json_str))


