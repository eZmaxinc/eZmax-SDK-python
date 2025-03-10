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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.field_e_systemconfiguration_ezsign import FieldESystemconfigurationEzsign
from eZmaxApi.models.field_e_systemconfiguration_ezsignofficeplan import FieldESystemconfigurationEzsignofficeplan
from eZmaxApi.models.field_e_systemconfiguration_language1 import FieldESystemconfigurationLanguage1
from eZmaxApi.models.field_e_systemconfiguration_language2 import FieldESystemconfigurationLanguage2
from eZmaxApi.models.field_e_systemconfiguration_newexternaluseraction import FieldESystemconfigurationNewexternaluseraction
from typing import Optional, Set
from typing_extensions import Self

class SystemconfigurationRequest(BaseModel):
    """
    A Systemconfiguration Object
    """ # noqa: E501
    pki_systemconfiguration_id: Optional[Annotated[int, Field(le=1, strict=True, ge=1)]] = Field(default=None, description="The unique ID of the Systemconfiguration", alias="pkiSystemconfigurationID")
    fki_branding_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Branding", alias="fkiBrandingID")
    e_systemconfiguration_newexternaluseraction: FieldESystemconfigurationNewexternaluseraction = Field(alias="eSystemconfigurationNewexternaluseraction")
    e_systemconfiguration_language1: FieldESystemconfigurationLanguage1 = Field(alias="eSystemconfigurationLanguage1")
    e_systemconfiguration_language2: FieldESystemconfigurationLanguage2 = Field(alias="eSystemconfigurationLanguage2")
    e_systemconfiguration_ezsign: Optional[FieldESystemconfigurationEzsign] = Field(default=None, alias="eSystemconfigurationEzsign")
    e_systemconfiguration_ezsignofficeplan: Optional[FieldESystemconfigurationEzsignofficeplan] = Field(default=None, alias="eSystemconfigurationEzsignofficeplan")
    b_systemconfiguration_ezsignpaidbyoffice: Optional[StrictBool] = Field(default=None, description="Whether if Ezsign is paid by the company or not", alias="bSystemconfigurationEzsignpaidbyoffice")
    b_systemconfiguration_ezsignpersonnal: StrictBool = Field(description="Whether if we allow the creation of personal files in eZsign", alias="bSystemconfigurationEzsignpersonnal")
    b_systemconfiguration_sspr: StrictBool = Field(description="Whether if we allow SSPR", alias="bSystemconfigurationSspr")
    dt_systemconfiguration_readonlyexpirationstart: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The start date where the system will be in read only", alias="dtSystemconfigurationReadonlyexpirationstart")
    dt_systemconfiguration_readonlyexpirationend: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The end date where the system will be in read only", alias="dtSystemconfigurationReadonlyexpirationend")
    __properties: ClassVar[List[str]] = ["pkiSystemconfigurationID", "fkiBrandingID", "eSystemconfigurationNewexternaluseraction", "eSystemconfigurationLanguage1", "eSystemconfigurationLanguage2", "eSystemconfigurationEzsign", "eSystemconfigurationEzsignofficeplan", "bSystemconfigurationEzsignpaidbyoffice", "bSystemconfigurationEzsignpersonnal", "bSystemconfigurationSspr", "dtSystemconfigurationReadonlyexpirationstart", "dtSystemconfigurationReadonlyexpirationend"]

    @field_validator('dt_systemconfiguration_readonlyexpirationstart')
    def dt_systemconfiguration_readonlyexpirationstart_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$/")
        return value

    @field_validator('dt_systemconfiguration_readonlyexpirationend')
    def dt_systemconfiguration_readonlyexpirationend_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$/")
        return value

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
        """Create an instance of SystemconfigurationRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SystemconfigurationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiSystemconfigurationID": obj.get("pkiSystemconfigurationID"),
            "fkiBrandingID": obj.get("fkiBrandingID"),
            "eSystemconfigurationNewexternaluseraction": obj.get("eSystemconfigurationNewexternaluseraction"),
            "eSystemconfigurationLanguage1": obj.get("eSystemconfigurationLanguage1"),
            "eSystemconfigurationLanguage2": obj.get("eSystemconfigurationLanguage2"),
            "eSystemconfigurationEzsign": obj.get("eSystemconfigurationEzsign"),
            "eSystemconfigurationEzsignofficeplan": obj.get("eSystemconfigurationEzsignofficeplan"),
            "bSystemconfigurationEzsignpaidbyoffice": obj.get("bSystemconfigurationEzsignpaidbyoffice"),
            "bSystemconfigurationEzsignpersonnal": obj.get("bSystemconfigurationEzsignpersonnal"),
            "bSystemconfigurationSspr": obj.get("bSystemconfigurationSspr"),
            "dtSystemconfigurationReadonlyexpirationstart": obj.get("dtSystemconfigurationReadonlyexpirationstart"),
            "dtSystemconfigurationReadonlyexpirationend": obj.get("dtSystemconfigurationReadonlyexpirationend")
        })
        return _obj


