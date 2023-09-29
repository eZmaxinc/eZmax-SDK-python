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





class FieldESessionhistoryEndby(str, Enum):
    """
    The Type of the Sessionhistory
    """

    """
    allowed enum values
    """
    DECRYPTION = 'Decryption'
    HACK = 'Hack'
    EXPIRED = 'Expired'
    HIJACK = 'Hijack'
    DOUBLELOGON = 'DoubleLogon'
    GARBAGE = 'Garbage'
    LOGOFF = 'Logoff'
    BADAUTH = 'BadAuth'
    LOCKED = 'Locked'
    INACTIVE = 'Inactive'
    INVALIDUSER = 'InvalidUser'
    BADUSERTYPE = 'BadUserType'
    BADIP = 'BadIP'
    FORCEDLOGOFF = 'ForcedLogoff'

    @classmethod
    def from_json(cls, json_str: str) -> FieldESessionhistoryEndby:
        """Create an instance of FieldESessionhistoryEndby from a JSON string"""
        return FieldESessionhistoryEndby(json.loads(json_str))

