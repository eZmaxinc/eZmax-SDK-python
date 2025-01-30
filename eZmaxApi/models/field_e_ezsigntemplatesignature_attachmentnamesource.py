# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.2
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class FieldEEzsigntemplatesignatureAttachmentnamesource(str, Enum):
    """
    The source of the name of the attachment added to the Ezsigntemplatesignature
    """

    """
    allowed enum values
    """
    DESCRIPTION = 'Description'
    CUSTOMER = 'Customer'
    DESCRIPTIONCUSTOMER = 'DescriptionCustomer'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FieldEEzsigntemplatesignatureAttachmentnamesource from a JSON string"""
        return cls(json.loads(json_str))


