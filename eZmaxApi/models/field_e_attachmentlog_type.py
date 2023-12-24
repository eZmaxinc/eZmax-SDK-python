# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class FieldEAttachmentlogType(str, Enum):
    """
    The Type for the Attachmentlog
    """

    """
    allowed enum values
    """
    AUTOVALIDATION = 'AutoValidation'
    COPYFROM = 'CopyFrom'
    COPYTO = 'CopyTo'
    COPYTOEZSIGN = 'CopyToEzsign'
    CREATEBYEZSIGN = 'CreateByEzsign'
    DOWNLOAD = 'Download'
    DELETED = 'Deleted'
    DESTROYED = 'Destroyed'
    EMAIL = 'Email'
    EMAILCC = 'EmailCC'
    EMAILCCI = 'EmailCCI'
    FAX = 'Fax'
    IMPORTEDFROMEXTERNALSYSTEM = 'ImportedFromExternalSystem'
    IMPORTEDFROMEZA = 'ImportedFromEZA'
    IMPORTEDFROMFALTOUR = 'ImportedFromFaltour'
    IMPORTEDFROMLONEWOLF = 'ImportedFromLonewolf'
    IMPORTEDFROMPROSPECTS = 'ImportedFromProspects'
    MOVE = 'Move'
    OPENFROMEMAIL = 'OpenFromEmail'
    PURGED = 'Purged'
    REJECT = 'Reject'
    RENAME = 'Rename'
    RESTORE = 'Restore'
    SCANNED = 'Scanned'
    SENDTOGED = 'SendToGED'
    UNVALIDATEDBY = 'UnvalidatedBy'
    UPLOAD = 'Upload'
    VALIDATEDBY = 'ValidatedBy'
    VETINFOUPLOAD = 'VetinfoUpload'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FieldEAttachmentlogType from a JSON string"""
        return cls(json.loads(json_str))


