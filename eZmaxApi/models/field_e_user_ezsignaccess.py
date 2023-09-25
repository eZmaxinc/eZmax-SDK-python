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





class FieldEUserEzsignaccess(str, Enum):
    """
    The type or eZsign access the User has
    """

    """
    allowed enum values
    """
    NO = 'No'
    PAIDBYOFFICE = 'PaidByOffice'
    PERDOCUMENT = 'PerDocument'
    PREPAID = 'Prepaid'

    @classmethod
    def from_json(cls, json_str: str) -> FieldEUserEzsignaccess:
        """Create an instance of FieldEUserEzsignaccess from a JSON string"""
        return FieldEUserEzsignaccess(json.loads(json_str))


