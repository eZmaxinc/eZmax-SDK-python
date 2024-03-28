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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.enum_textvalidation import EnumTextvalidation
from eZmaxApi.models.field_e_ezsignformfieldgroup_signerrequirement import FieldEEzsignformfieldgroupSignerrequirement
from eZmaxApi.models.field_e_ezsignformfieldgroup_tooltipposition import FieldEEzsignformfieldgroupTooltipposition
from eZmaxApi.models.field_e_ezsignformfieldgroup_type import FieldEEzsignformfieldgroupType
from typing import Optional, Set
from typing_extensions import Self

class EzsignformfieldgroupRequest(BaseModel):
    """
    An Ezsignformfieldgroup Object
    """ # noqa: E501
    pki_ezsignformfieldgroup_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The unique ID of the Ezsignformfieldgroup", alias="pkiEzsignformfieldgroupID")
    fki_ezsigndocument_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigndocument", alias="fkiEzsigndocumentID")
    e_ezsignformfieldgroup_type: FieldEEzsignformfieldgroupType = Field(alias="eEzsignformfieldgroupType")
    e_ezsignformfieldgroup_signerrequirement: Optional[FieldEEzsignformfieldgroupSignerrequirement] = Field(default=None, alias="eEzsignformfieldgroupSignerrequirement")
    s_ezsignformfieldgroup_label: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="The Label for the Ezsignformfieldgroup", alias="sEzsignformfieldgroupLabel")
    i_ezsignformfieldgroup_step: Annotated[int, Field(strict=True, ge=1)] = Field(description="The step when the Ezsignsigner will be invited to fill the form fields", alias="iEzsignformfieldgroupStep")
    s_ezsignformfieldgroup_defaultvalue: Optional[StrictStr] = Field(default=None, description="The default value for the Ezsignformfieldgroup  You can use the codes below and they will be replaced at signature time.    | Code | Description | Example | | ------------------------- | ------------ | ------------ | | {sUserFirstname} | The first name of the contact | John | | {sUserLastname} | The last name of the contact | Doe | | {sUserJobtitle} | The job title | Sales Representative | | {sEmailAddress} | The email address | email@example.com | | {sPhoneE164} | A phone number in E.164 Format | +15149901516 | | {sPhoneE164Cell} | A phone number in E.164 Format | +15149901516 |", alias="sEzsignformfieldgroupDefaultvalue")
    i_ezsignformfieldgroup_filledmin: Annotated[int, Field(strict=True, ge=0)] = Field(description="The minimum number of Ezsignformfield that must be filled in the Ezsignformfieldgroup", alias="iEzsignformfieldgroupFilledmin")
    i_ezsignformfieldgroup_filledmax: Annotated[int, Field(strict=True, ge=0)] = Field(description="The maximum number of Ezsignformfield that must be filled in the Ezsignformfieldgroup", alias="iEzsignformfieldgroupFilledmax")
    b_ezsignformfieldgroup_readonly: StrictBool = Field(description="Whether the Ezsignformfieldgroup is read only or not.", alias="bEzsignformfieldgroupReadonly")
    i_ezsignformfieldgroup_maxlength: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The maximum length for the value in the Ezsignformfieldgroup  This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea**", alias="iEzsignformfieldgroupMaxlength")
    b_ezsignformfieldgroup_encrypted: Optional[StrictBool] = Field(default=None, description="Whether the Ezsignformfieldgroup is encrypted in the database or not. Encrypted values are not displayed on the Ezsigndocument. This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea**", alias="bEzsignformfieldgroupEncrypted")
    s_ezsignformfieldgroup_regexp: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A regular expression to indicate what values are acceptable for the Ezsignformfieldgroup.  This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea**", alias="sEzsignformfieldgroupRegexp")
    t_ezsignformfieldgroup_tooltip: Optional[StrictStr] = Field(default=None, description="A tooltip that will be presented to Ezsignsigner about the Ezsignformfieldgroup", alias="tEzsignformfieldgroupTooltip")
    e_ezsignformfieldgroup_tooltipposition: Optional[FieldEEzsignformfieldgroupTooltipposition] = Field(default=None, alias="eEzsignformfieldgroupTooltipposition")
    e_ezsignformfieldgroup_textvalidation: Optional[EnumTextvalidation] = Field(default=None, alias="eEzsignformfieldgroupTextvalidation")
    __properties: ClassVar[List[str]] = ["pkiEzsignformfieldgroupID", "fkiEzsigndocumentID", "eEzsignformfieldgroupType", "eEzsignformfieldgroupSignerrequirement", "sEzsignformfieldgroupLabel", "iEzsignformfieldgroupStep", "sEzsignformfieldgroupDefaultvalue", "iEzsignformfieldgroupFilledmin", "iEzsignformfieldgroupFilledmax", "bEzsignformfieldgroupReadonly", "iEzsignformfieldgroupMaxlength", "bEzsignformfieldgroupEncrypted", "sEzsignformfieldgroupRegexp", "tEzsignformfieldgroupTooltip", "eEzsignformfieldgroupTooltipposition", "eEzsignformfieldgroupTextvalidation"]

    @field_validator('s_ezsignformfieldgroup_regexp')
    def s_ezsignformfieldgroup_regexp_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\^.*\$$|^$", value):
            raise ValueError(r"must validate the regular expression /^\^.*\$$|^$/")
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
        """Create an instance of EzsignformfieldgroupRequest from a JSON string"""
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
        """Create an instance of EzsignformfieldgroupRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignformfieldgroupID": obj.get("pkiEzsignformfieldgroupID"),
            "fkiEzsigndocumentID": obj.get("fkiEzsigndocumentID"),
            "eEzsignformfieldgroupType": obj.get("eEzsignformfieldgroupType"),
            "eEzsignformfieldgroupSignerrequirement": obj.get("eEzsignformfieldgroupSignerrequirement"),
            "sEzsignformfieldgroupLabel": obj.get("sEzsignformfieldgroupLabel"),
            "iEzsignformfieldgroupStep": obj.get("iEzsignformfieldgroupStep"),
            "sEzsignformfieldgroupDefaultvalue": obj.get("sEzsignformfieldgroupDefaultvalue"),
            "iEzsignformfieldgroupFilledmin": obj.get("iEzsignformfieldgroupFilledmin"),
            "iEzsignformfieldgroupFilledmax": obj.get("iEzsignformfieldgroupFilledmax"),
            "bEzsignformfieldgroupReadonly": obj.get("bEzsignformfieldgroupReadonly"),
            "iEzsignformfieldgroupMaxlength": obj.get("iEzsignformfieldgroupMaxlength"),
            "bEzsignformfieldgroupEncrypted": obj.get("bEzsignformfieldgroupEncrypted"),
            "sEzsignformfieldgroupRegexp": obj.get("sEzsignformfieldgroupRegexp"),
            "tEzsignformfieldgroupTooltip": obj.get("tEzsignformfieldgroupTooltip"),
            "eEzsignformfieldgroupTooltipposition": obj.get("eEzsignformfieldgroupTooltipposition"),
            "eEzsignformfieldgroupTextvalidation": obj.get("eEzsignformfieldgroupTextvalidation")
        })
        return _obj


