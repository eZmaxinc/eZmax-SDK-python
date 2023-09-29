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





class FieldEEzsignfoldertypeSendreminderfrequency(str, Enum):
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
    def from_json(cls, json_str: str) -> FieldEEzsignfoldertypeSendreminderfrequency:
        """Create an instance of FieldEEzsignfoldertypeSendreminderfrequency from a JSON string"""
        return FieldEEzsignfoldertypeSendreminderfrequency(json.loads(json_str))

