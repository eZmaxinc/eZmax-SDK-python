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





class FieldEEzsigndocumentStep(str, Enum):
    """
    The signature step of the Ezsigndocument.
    """

    """
    allowed enum values
    """
    UNSENT = 'Unsent'
    UNSIGNED = 'Unsigned'
    PARTIALLYSIGNED = 'PartiallySigned'
    DECLINEDTOSIGN = 'DeclinedToSign'
    PREMATURELYENDED = 'PrematurelyEnded'
    COMPLETED = 'Completed'
    DISPOSED = 'Disposed'

    @classmethod
    def from_json(cls, json_str: str) -> FieldEEzsigndocumentStep:
        """Create an instance of FieldEEzsigndocumentStep from a JSON string"""
        return FieldEEzsigndocumentStep(json.loads(json_str))


