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





class FieldEVersionhistoryUsertype(str, Enum):
    """
    The Usertype by which the Versionhistory should be visible
    """

    """
    allowed enum values
    """
    EMPTY = ''
    AGENTBROKER = 'AgentBroker'
    EZSIGNUSER = 'EzsignUser'
    NORMAL = 'Normal'

    @classmethod
    def from_json(cls, json_str: str) -> FieldEVersionhistoryUsertype:
        """Create an instance of FieldEVersionhistoryUsertype from a JSON string"""
        return FieldEVersionhistoryUsertype(json.loads(json_str))


