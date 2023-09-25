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





class FieldECommunicationImportance(str, Enum):
    """
    The importance of the Communication
    """

    """
    allowed enum values
    """
    HIGH = 'High'
    NORMAL = 'Normal'
    LOW = 'Low'

    @classmethod
    def from_json(cls, json_str: str) -> FieldECommunicationImportance:
        """Create an instance of FieldECommunicationImportance from a JSON string"""
        return FieldECommunicationImportance(json.loads(json_str))


