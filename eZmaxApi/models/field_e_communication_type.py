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





class FieldECommunicationType(str, Enum):
    """
    The type of the Communication
    """

    """
    allowed enum values
    """
    EMAIL = 'Email'
    FAX = 'Fax'
    SMS = 'Sms'

    @classmethod
    def from_json(cls, json_str: str) -> FieldECommunicationType:
        """Create an instance of FieldECommunicationType from a JSON string"""
        return FieldECommunicationType(json.loads(json_str))

