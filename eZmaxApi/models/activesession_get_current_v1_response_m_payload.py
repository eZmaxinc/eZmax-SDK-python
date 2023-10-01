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
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, conlist, constr
from eZmaxApi.models.activesession_response_compound_apikey import ActivesessionResponseCompoundApikey
from eZmaxApi.models.activesession_response_compound_user import ActivesessionResponseCompoundUser
from eZmaxApi.models.field_e_activesession_origin import FieldEActivesessionOrigin
from eZmaxApi.models.field_e_activesession_usertype import FieldEActivesessionUsertype
from eZmaxApi.models.field_e_activesession_weekdaystart import FieldEActivesessionWeekdaystart

class ActivesessionGetCurrentV1ResponseMPayload(BaseModel):
    """
    Payload for GET /1/object/activesession/getCurrent  # noqa: E501
    """
    e_activesession_usertype: FieldEActivesessionUsertype = Field(..., alias="eActivesessionUsertype")
    e_activesession_origin: FieldEActivesessionOrigin = Field(..., alias="eActivesessionOrigin")
    e_activesession_weekdaystart: FieldEActivesessionWeekdaystart = Field(..., alias="eActivesessionWeekdaystart")
    fki_language_id: conint(strict=True, le=2, ge=1) = Field(..., alias="fkiLanguageID", description="The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English|")
    s_company_name_x: StrictStr = Field(..., alias="sCompanyNameX", description="The Name of the Company in the language of the requester")
    s_department_name_x: StrictStr = Field(..., alias="sDepartmentNameX", description="The Name of the Department in the language of the requester")
    b_activesession_debug: StrictBool = Field(..., alias="bActivesessionDebug", description="Whether the active session is in debug or not")
    b_activesession_issuperadmin: StrictBool = Field(..., alias="bActivesessionIssuperadmin", description="Whether the active session is superadmin or not")
    pks_customer_code: constr(strict=True, max_length=6, min_length=2) = Field(..., alias="pksCustomerCode", description="The customer code assigned to your account")
    fki_systemconfigurationtype_id: conint(strict=True, ge=1) = Field(..., alias="fkiSystemconfigurationtypeID", description="The unique ID of the Systemconfigurationtype")
    fki_signature_id: Optional[conint(strict=True, le=16777215, ge=0)] = Field(None, alias="fkiSignatureID", description="The unique ID of the Signature")
    a_pki_permission_id: conlist(conint(strict=True, ge=0)) = Field(..., alias="a_pkiPermissionID", description="An array of permissions granted to the user or api key")
    obj_user_real: ActivesessionResponseCompoundUser = Field(..., alias="objUserReal")
    obj_user_cloned: Optional[ActivesessionResponseCompoundUser] = Field(None, alias="objUserCloned")
    obj_apikey: Optional[ActivesessionResponseCompoundApikey] = Field(None, alias="objApikey")
    a_e_module_internalname: conlist(StrictStr) = Field(..., alias="a_eModuleInternalname", description="An Array of Registered modules.  These are the modules that are Licensed to be used by the User or the API Key.")
    __properties = ["eActivesessionUsertype", "eActivesessionOrigin", "eActivesessionWeekdaystart", "fkiLanguageID", "sCompanyNameX", "sDepartmentNameX", "bActivesessionDebug", "bActivesessionIssuperadmin", "pksCustomerCode", "fkiSystemconfigurationtypeID", "fkiSignatureID", "a_pkiPermissionID", "objUserReal", "objUserCloned", "objApikey", "a_eModuleInternalname"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ActivesessionGetCurrentV1ResponseMPayload:
        """Create an instance of ActivesessionGetCurrentV1ResponseMPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_user_real
        if self.obj_user_real:
            _dict['objUserReal'] = self.obj_user_real.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_user_cloned
        if self.obj_user_cloned:
            _dict['objUserCloned'] = self.obj_user_cloned.to_dict()
        # override the default output from pydantic by calling `to_dict()` of obj_apikey
        if self.obj_apikey:
            _dict['objApikey'] = self.obj_apikey.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ActivesessionGetCurrentV1ResponseMPayload:
        """Create an instance of ActivesessionGetCurrentV1ResponseMPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ActivesessionGetCurrentV1ResponseMPayload.parse_obj(obj)

        _obj = ActivesessionGetCurrentV1ResponseMPayload.parse_obj({
            "e_activesession_usertype": obj.get("eActivesessionUsertype"),
            "e_activesession_origin": obj.get("eActivesessionOrigin"),
            "e_activesession_weekdaystart": obj.get("eActivesessionWeekdaystart"),
            "fki_language_id": obj.get("fkiLanguageID"),
            "s_company_name_x": obj.get("sCompanyNameX"),
            "s_department_name_x": obj.get("sDepartmentNameX"),
            "b_activesession_debug": obj.get("bActivesessionDebug"),
            "b_activesession_issuperadmin": obj.get("bActivesessionIssuperadmin"),
            "pks_customer_code": obj.get("pksCustomerCode"),
            "fki_systemconfigurationtype_id": obj.get("fkiSystemconfigurationtypeID"),
            "fki_signature_id": obj.get("fkiSignatureID"),
            "a_pki_permission_id": obj.get("a_pkiPermissionID"),
            "obj_user_real": ActivesessionResponseCompoundUser.from_dict(obj.get("objUserReal")) if obj.get("objUserReal") is not None else None,
            "obj_user_cloned": ActivesessionResponseCompoundUser.from_dict(obj.get("objUserCloned")) if obj.get("objUserCloned") is not None else None,
            "obj_apikey": ActivesessionResponseCompoundApikey.from_dict(obj.get("objApikey")) if obj.get("objApikey") is not None else None,
            "a_e_module_internalname": obj.get("a_eModuleInternalname")
        })
        return _obj


