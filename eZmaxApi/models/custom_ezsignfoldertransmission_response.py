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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from eZmaxApi.models.custom_ezsignfoldertransmission_signer_response import CustomEzsignfoldertransmissionSignerResponse
from eZmaxApi.models.field_e_ezsignfolder_step import FieldEEzsignfolderStep
from typing import Optional, Set
from typing_extensions import Self

class CustomEzsignfoldertransmissionResponse(BaseModel):
    """
    An Ezsignfolder Object in the context of an Ezsignbulksendtransmission
    """ # noqa: E501
    pki_ezsignfolder_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignfolder", alias="pkiEzsignfolderID")
    s_ezsignfolder_description: Annotated[str, Field(strict=True)] = Field(description="The description of the Ezsignfolder", alias="sEzsignfolderDescription")
    e_ezsignfolder_step: FieldEEzsignfolderStep = Field(alias="eEzsignfolderStep")
    i_ezsignfolder_signaturetotal: StrictInt = Field(description="The number of total signatures that were requested in the Ezsignfolder", alias="iEzsignfolderSignaturetotal")
    i_ezsignfolder_formfieldtotal: StrictInt = Field(description="The number of total form fields that were requested in the Ezsignfolder", alias="iEzsignfolderFormfieldtotal")
    i_ezsignfolder_signaturesigned: StrictInt = Field(description="The number of signatures that were signed in the Ezsignfolder.", alias="iEzsignfolderSignaturesigned")
    a_obj_ezsignfoldertransmission_signer: List[CustomEzsignfoldertransmissionSignerResponse] = Field(alias="a_objEzsignfoldertransmissionSigner")
    __properties: ClassVar[List[str]] = ["pkiEzsignfolderID", "sEzsignfolderDescription", "eEzsignfolderStep", "iEzsignfolderSignaturetotal", "iEzsignfolderFormfieldtotal", "iEzsignfolderSignaturesigned", "a_objEzsignfoldertransmissionSigner"]

    @field_validator('s_ezsignfolder_description')
    def s_ezsignfolder_description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,75}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,75}$/")
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
        """Create an instance of CustomEzsignfoldertransmissionResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in a_obj_ezsignfoldertransmission_signer (list)
        _items = []
        if self.a_obj_ezsignfoldertransmission_signer:
            for _item_a_obj_ezsignfoldertransmission_signer in self.a_obj_ezsignfoldertransmission_signer:
                if _item_a_obj_ezsignfoldertransmission_signer:
                    _items.append(_item_a_obj_ezsignfoldertransmission_signer.to_dict())
            _dict['a_objEzsignfoldertransmissionSigner'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomEzsignfoldertransmissionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignfolderID": obj.get("pkiEzsignfolderID"),
            "sEzsignfolderDescription": obj.get("sEzsignfolderDescription"),
            "eEzsignfolderStep": obj.get("eEzsignfolderStep"),
            "iEzsignfolderSignaturetotal": obj.get("iEzsignfolderSignaturetotal"),
            "iEzsignfolderFormfieldtotal": obj.get("iEzsignfolderFormfieldtotal"),
            "iEzsignfolderSignaturesigned": obj.get("iEzsignfolderSignaturesigned"),
            "a_objEzsignfoldertransmissionSigner": [CustomEzsignfoldertransmissionSignerResponse.from_dict(_item) for _item in obj["a_objEzsignfoldertransmissionSigner"]] if obj.get("a_objEzsignfoldertransmissionSigner") is not None else None
        })
        return _obj


