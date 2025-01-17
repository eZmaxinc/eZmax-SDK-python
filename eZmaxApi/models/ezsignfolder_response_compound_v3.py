# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.1
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from eZmaxApi.models.common_audit import CommonAudit
from eZmaxApi.models.computed_e_ezsignfolder_access import ComputedEEzsignfolderAccess
from eZmaxApi.models.custom_ezsignfoldertype_response import CustomEzsignfoldertypeResponse
from eZmaxApi.models.custom_timezone_with_code_response import CustomTimezoneWithCodeResponse
from eZmaxApi.models.ezsignfolder_response_v3 import EzsignfolderResponseV3
from eZmaxApi.models.field_e_ezsignfolder_completion import FieldEEzsignfolderCompletion
from eZmaxApi.models.field_e_ezsignfolder_documentdependency import FieldEEzsignfolderDocumentdependency
from eZmaxApi.models.field_e_ezsignfolder_step import FieldEEzsignfolderStep
from typing import Optional, Set
from typing_extensions import Self

class EzsignfolderResponseCompoundV3(EzsignfolderResponseV3):
    """
    An Ezsignfolder Object and children to create a complete structure
    """ # noqa: E501
    obj_timezone: Optional[CustomTimezoneWithCodeResponse] = Field(default=None, alias="objTimezone")
    __properties: ClassVar[List[str]] = ["pkiEzsignfolderID", "fkiEzsignfoldertypeID", "objEzsignfoldertype", "fkiTimezoneID", "eEzsignfolderCompletion", "eEzsignfolderDocumentdependency", "sEzsignfoldertypeNameX", "fkiBillingentityinternalID", "sBillingentityinternalDescriptionX", "fkiEzsigntsarequirementID", "sEzsigntsarequirementDescriptionX", "sEzsignfolderDescription", "tEzsignfolderNote", "bEzsignfolderIsdisposable", "iEzsignfolderSendreminderfirstdays", "iEzsignfolderSendreminderotherdays", "dtEzsignfolderDelayedsenddate", "dtEzsignfolderDuedate", "dtEzsignfolderSentdate", "dtEzsignfolderScheduledarchive", "dtEzsignfolderScheduleddispose", "eEzsignfolderStep", "dtEzsignfolderClose", "tEzsignfolderMessage", "objAudit", "sEzsignfolderExternalid", "eEzsignfolderAccess", "objTimezone"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EzsignfolderResponseCompoundV3 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of obj_ezsignfoldertype
        if self.obj_ezsignfoldertype:
            _dict['objEzsignfoldertype'] = self.obj_ezsignfoldertype.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_audit
        if self.obj_audit:
            _dict['objAudit'] = self.obj_audit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_timezone
        if self.obj_timezone:
            _dict['objTimezone'] = self.obj_timezone.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EzsignfolderResponseCompoundV3 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignfolderID": obj.get("pkiEzsignfolderID"),
            "fkiEzsignfoldertypeID": obj.get("fkiEzsignfoldertypeID"),
            "objEzsignfoldertype": CustomEzsignfoldertypeResponse.from_dict(obj["objEzsignfoldertype"]) if obj.get("objEzsignfoldertype") is not None else None,
            "fkiTimezoneID": obj.get("fkiTimezoneID"),
            "eEzsignfolderCompletion": obj.get("eEzsignfolderCompletion"),
            "eEzsignfolderDocumentdependency": obj.get("eEzsignfolderDocumentdependency"),
            "sEzsignfoldertypeNameX": obj.get("sEzsignfoldertypeNameX"),
            "fkiBillingentityinternalID": obj.get("fkiBillingentityinternalID"),
            "sBillingentityinternalDescriptionX": obj.get("sBillingentityinternalDescriptionX"),
            "fkiEzsigntsarequirementID": obj.get("fkiEzsigntsarequirementID"),
            "sEzsigntsarequirementDescriptionX": obj.get("sEzsigntsarequirementDescriptionX"),
            "sEzsignfolderDescription": obj.get("sEzsignfolderDescription"),
            "tEzsignfolderNote": obj.get("tEzsignfolderNote"),
            "bEzsignfolderIsdisposable": obj.get("bEzsignfolderIsdisposable"),
            "iEzsignfolderSendreminderfirstdays": obj.get("iEzsignfolderSendreminderfirstdays"),
            "iEzsignfolderSendreminderotherdays": obj.get("iEzsignfolderSendreminderotherdays"),
            "dtEzsignfolderDelayedsenddate": obj.get("dtEzsignfolderDelayedsenddate"),
            "dtEzsignfolderDuedate": obj.get("dtEzsignfolderDuedate"),
            "dtEzsignfolderSentdate": obj.get("dtEzsignfolderSentdate"),
            "dtEzsignfolderScheduledarchive": obj.get("dtEzsignfolderScheduledarchive"),
            "dtEzsignfolderScheduleddispose": obj.get("dtEzsignfolderScheduleddispose"),
            "eEzsignfolderStep": obj.get("eEzsignfolderStep"),
            "dtEzsignfolderClose": obj.get("dtEzsignfolderClose"),
            "tEzsignfolderMessage": obj.get("tEzsignfolderMessage"),
            "objAudit": CommonAudit.from_dict(obj["objAudit"]) if obj.get("objAudit") is not None else None,
            "sEzsignfolderExternalid": obj.get("sEzsignfolderExternalid"),
            "eEzsignfolderAccess": obj.get("eEzsignfolderAccess"),
            "objTimezone": CustomTimezoneWithCodeResponse.from_dict(obj["objTimezone"]) if obj.get("objTimezone") is not None else None
        })
        return _obj


