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





class FieldEEzmaxinvoicingagentVariationezmax(str, Enum):
    """
    Variation type for eZmax
    """

    """
    allowed enum values
    """
    CHARGE = 'Charge'
    REFUND = 'Refund'
    SAME = 'Same'

    @classmethod
    def from_json(cls, json_str: str) -> FieldEEzmaxinvoicingagentVariationezmax:
        """Create an instance of FieldEEzmaxinvoicingagentVariationezmax from a JSON string"""
        return FieldEEzmaxinvoicingagentVariationezmax(json.loads(json_str))


