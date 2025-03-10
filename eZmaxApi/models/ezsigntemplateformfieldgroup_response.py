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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eZmaxApi.models.enum_textvalidation import EnumTextvalidation
from eZmaxApi.models.field_e_ezsigntemplateformfieldgroup_signerrequirement import FieldEEzsigntemplateformfieldgroupSignerrequirement
from eZmaxApi.models.field_e_ezsigntemplateformfieldgroup_tooltipposition import FieldEEzsigntemplateformfieldgroupTooltipposition
from eZmaxApi.models.field_e_ezsigntemplateformfieldgroup_type import FieldEEzsigntemplateformfieldgroupType
from typing import Optional, Set
from typing_extensions import Self

class EzsigntemplateformfieldgroupResponse(BaseModel):
    """
    A Ezsigntemplateformfieldgroup Object
    """ # noqa: E501
    pki_ezsigntemplateformfieldgroup_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplateformfieldgroup", alias="pkiEzsigntemplateformfieldgroupID")
    fki_ezsigntemplatedocument_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsigntemplatedocument", alias="fkiEzsigntemplatedocumentID")
    e_ezsigntemplateformfieldgroup_type: FieldEEzsigntemplateformfieldgroupType = Field(alias="eEzsigntemplateformfieldgroupType")
    e_ezsigntemplateformfieldgroup_signerrequirement: Optional[FieldEEzsigntemplateformfieldgroupSignerrequirement] = Field(default=None, alias="eEzsigntemplateformfieldgroupSignerrequirement")
    s_ezsigntemplateformfieldgroup_label: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="The Label for the Ezsigntemplateformfieldgroup", alias="sEzsigntemplateformfieldgroupLabel")
    i_ezsigntemplateformfieldgroup_step: Annotated[int, Field(strict=True, ge=1)] = Field(description="The step when the Ezsigntemplatesigner will be invited to fill the form fields", alias="iEzsigntemplateformfieldgroupStep")
    s_ezsigntemplateformfieldgroup_defaultvalue: Optional[StrictStr] = Field(default=None, description="The default value for the Ezsigntemplateformfieldgroup  You can use the codes below and they will be replaced at signature time.    | Code | Description | Example | | ------------------------- | ------------ | ------------ | | {sUserFirstname} | The first name of the contact | John | | {sUserLastname} | The last name of the contact | Doe | | {sUserJobtitle} | The job title | Sales Representative | | {sEmailAddress} | The email address | email@example.com | | {sPhoneE164} | A phone number in E.164 Format | +15149901516 | | {sPhoneE164Cell} | A phone number in E.164 Format | +15149901516 |", alias="sEzsigntemplateformfieldgroupDefaultvalue")
    i_ezsigntemplateformfieldgroup_filledmin: Annotated[int, Field(strict=True, ge=0)] = Field(description="The minimum number of Ezsigntemplateformfield that must be filled in the Ezsigntemplateformfieldgroup", alias="iEzsigntemplateformfieldgroupFilledmin")
    i_ezsigntemplateformfieldgroup_filledmax: Annotated[int, Field(strict=True, ge=0)] = Field(description="The maximum number of Ezsigntemplateformfield that must be filled in the Ezsigntemplateformfieldgroup", alias="iEzsigntemplateformfieldgroupFilledmax")
    b_ezsigntemplateformfieldgroup_readonly: StrictBool = Field(description="Whether the Ezsigntemplateformfieldgroup is read only or not.", alias="bEzsigntemplateformfieldgroupReadonly")
    i_ezsigntemplateformfieldgroup_maxlength: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The maximum length for the value in the Ezsigntemplateformfieldgroup  This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea**", alias="iEzsigntemplateformfieldgroupMaxlength")
    b_ezsigntemplateformfieldgroup_encrypted: Optional[StrictBool] = Field(default=None, description="Whether the Ezsigntemplateformfieldgroup is encrypted in the database or not. Encrypted values are not displayed on the Ezsigndocument. This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea**", alias="bEzsigntemplateformfieldgroupEncrypted")
    s_ezsigntemplateformfieldgroup_regexp: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A regular expression to indicate what values are acceptable for the Ezsigntemplateformfieldgroup.  This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea**", alias="sEzsigntemplateformfieldgroupRegexp")
    s_ezsigntemplateformfieldgroup_textvalidationcustommessage: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="Description of validation rule. Show by signatory.", alias="sEzsigntemplateformfieldgroupTextvalidationcustommessage")
    e_ezsigntemplateformfieldgroup_textvalidation: Optional[EnumTextvalidation] = Field(default=None, alias="eEzsigntemplateformfieldgroupTextvalidation")
    t_ezsigntemplateformfieldgroup_tooltip: Optional[StrictStr] = Field(default=None, description="A tooltip that will be presented to Ezsigntemplatesigner about the Ezsigntemplateformfieldgroup", alias="tEzsigntemplateformfieldgroupTooltip")
    e_ezsigntemplateformfieldgroup_tooltipposition: Optional[FieldEEzsigntemplateformfieldgroupTooltipposition] = Field(default=None, alias="eEzsigntemplateformfieldgroupTooltipposition")
    __properties: ClassVar[List[str]] = ["pkiEzsigntemplateformfieldgroupID", "fkiEzsigntemplatedocumentID", "eEzsigntemplateformfieldgroupType", "eEzsigntemplateformfieldgroupSignerrequirement", "sEzsigntemplateformfieldgroupLabel", "iEzsigntemplateformfieldgroupStep", "sEzsigntemplateformfieldgroupDefaultvalue", "iEzsigntemplateformfieldgroupFilledmin", "iEzsigntemplateformfieldgroupFilledmax", "bEzsigntemplateformfieldgroupReadonly", "iEzsigntemplateformfieldgroupMaxlength", "bEzsigntemplateformfieldgroupEncrypted", "sEzsigntemplateformfieldgroupRegexp", "sEzsigntemplateformfieldgroupTextvalidationcustommessage", "eEzsigntemplateformfieldgroupTextvalidation", "tEzsigntemplateformfieldgroupTooltip", "eEzsigntemplateformfieldgroupTooltipposition"]

    @field_validator('s_ezsigntemplateformfieldgroup_regexp')
    def s_ezsigntemplateformfieldgroup_regexp_validate_regular_expression(cls, value):
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
        """Create an instance of EzsigntemplateformfieldgroupResponse from a JSON string"""
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
        """Create an instance of EzsigntemplateformfieldgroupResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsigntemplateformfieldgroupID": obj.get("pkiEzsigntemplateformfieldgroupID"),
            "fkiEzsigntemplatedocumentID": obj.get("fkiEzsigntemplatedocumentID"),
            "eEzsigntemplateformfieldgroupType": obj.get("eEzsigntemplateformfieldgroupType"),
            "eEzsigntemplateformfieldgroupSignerrequirement": obj.get("eEzsigntemplateformfieldgroupSignerrequirement"),
            "sEzsigntemplateformfieldgroupLabel": obj.get("sEzsigntemplateformfieldgroupLabel"),
            "iEzsigntemplateformfieldgroupStep": obj.get("iEzsigntemplateformfieldgroupStep"),
            "sEzsigntemplateformfieldgroupDefaultvalue": obj.get("sEzsigntemplateformfieldgroupDefaultvalue"),
            "iEzsigntemplateformfieldgroupFilledmin": obj.get("iEzsigntemplateformfieldgroupFilledmin"),
            "iEzsigntemplateformfieldgroupFilledmax": obj.get("iEzsigntemplateformfieldgroupFilledmax"),
            "bEzsigntemplateformfieldgroupReadonly": obj.get("bEzsigntemplateformfieldgroupReadonly"),
            "iEzsigntemplateformfieldgroupMaxlength": obj.get("iEzsigntemplateformfieldgroupMaxlength"),
            "bEzsigntemplateformfieldgroupEncrypted": obj.get("bEzsigntemplateformfieldgroupEncrypted"),
            "sEzsigntemplateformfieldgroupRegexp": obj.get("sEzsigntemplateformfieldgroupRegexp"),
            "sEzsigntemplateformfieldgroupTextvalidationcustommessage": obj.get("sEzsigntemplateformfieldgroupTextvalidationcustommessage"),
            "eEzsigntemplateformfieldgroupTextvalidation": obj.get("eEzsigntemplateformfieldgroupTextvalidation"),
            "tEzsigntemplateformfieldgroupTooltip": obj.get("tEzsigntemplateformfieldgroupTooltip"),
            "eEzsigntemplateformfieldgroupTooltipposition": obj.get("eEzsigntemplateformfieldgroupTooltipposition")
        })
        return _obj


