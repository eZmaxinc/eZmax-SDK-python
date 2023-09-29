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





class FieldEEzsigntemplatesignatureType(str, Enum):
    """
    The type of signature.  1. **Acknowledgement** is for an acknowledgment of receipt. 2. **City** is to request the city where the document is signed. 3. **Handwritten** is for a handwritten kind of signature where users needs to \"draw\" their signature on screen. 4. **Initials** is a simple \"click to add initials\" block. 5. **Name** is a simple \"Click to sign\" block. This is the most common block of signature. 6. **Attachments** is to ask for files as attachment that may be validate in another step.    
    """

    """
    allowed enum values
    """
    ACKNOWLEDGEMENT = 'Acknowledgement'
    CITY = 'City'
    HANDWRITTEN = 'Handwritten'
    INITIALS = 'Initials'
    NAME = 'Name'
    ATTACHMENTS = 'Attachments'
    FIELDTEXT = 'FieldText'
    FIELDTEXTAREA = 'FieldTextarea'

    @classmethod
    def from_json(cls, json_str: str) -> FieldEEzsigntemplatesignatureType:
        """Create an instance of FieldEEzsigntemplatesignatureType from a JSON string"""
        return FieldEEzsigntemplatesignatureType(json.loads(json_str))

