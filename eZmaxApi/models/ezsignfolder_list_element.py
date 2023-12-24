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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from eZmaxApi.models.field_e_ezsignfolder_step import FieldEEzsignfolderStep
from eZmaxApi.models.field_e_ezsignfoldertype_privacylevel import FieldEEzsignfoldertypePrivacylevel
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EzsignfolderListElement(BaseModel):
    """
    An Ezsignfolder List Element
    """ # noqa: E501
    pki_ezsignfolder_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignfolder", alias="pkiEzsignfolderID")
    fki_ezsignfoldertype_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Ezsignfoldertype.", alias="fkiEzsignfoldertypeID")
    e_ezsignfoldertype_privacylevel: FieldEEzsignfoldertypePrivacylevel = Field(alias="eEzsignfoldertypePrivacylevel")
    s_ezsignfoldertype_name_x: StrictStr = Field(description="The name of the Ezsignfoldertype in the language of the requester", alias="sEzsignfoldertypeNameX")
    s_ezsignfolder_description: StrictStr = Field(description="The description of the Ezsignfolder", alias="sEzsignfolderDescription")
    e_ezsignfolder_step: FieldEEzsignfolderStep = Field(alias="eEzsignfolderStep")
    dt_created_date: StrictStr = Field(description="The date and time at which the object was created", alias="dtCreatedDate")
    dt_ezsignfolder_sentdate: Optional[StrictStr] = Field(default=None, description="The date and time at which the Ezsignfolder was sent the last time.", alias="dtEzsignfolderSentdate")
    dt_ezsignfolder_duedate: Optional[StrictStr] = Field(default=None, description="The maximum date and time at which the Ezsignfolder can be signed.", alias="dtEzsignfolderDuedate")
    i_ezsigndocument: StrictInt = Field(description="The total number of Ezsigndocument in the folder", alias="iEzsigndocument")
    i_ezsigndocument_edm: StrictInt = Field(description="The total number of Ezsigndocument in the folder that were saved in the edm system", alias="iEzsigndocumentEdm")
    i_ezsignsignature: StrictInt = Field(description="The total number of signature blocks in all Ezsigndocuments in the folder", alias="iEzsignsignature")
    i_ezsignsignature_signed: StrictInt = Field(description="The total number of already signed signature blocks in all Ezsigndocuments in the folder", alias="iEzsignsignatureSigned")
    __properties: ClassVar[List[str]] = ["pkiEzsignfolderID", "fkiEzsignfoldertypeID", "eEzsignfoldertypePrivacylevel", "sEzsignfoldertypeNameX", "sEzsignfolderDescription", "eEzsignfolderStep", "dtCreatedDate", "dtEzsignfolderSentdate", "dtEzsignfolderDuedate", "iEzsigndocument", "iEzsigndocumentEdm", "iEzsignsignature", "iEzsignsignatureSigned"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EzsignfolderListElement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EzsignfolderListElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiEzsignfolderID": obj.get("pkiEzsignfolderID"),
            "fkiEzsignfoldertypeID": obj.get("fkiEzsignfoldertypeID"),
            "eEzsignfoldertypePrivacylevel": obj.get("eEzsignfoldertypePrivacylevel"),
            "sEzsignfoldertypeNameX": obj.get("sEzsignfoldertypeNameX"),
            "sEzsignfolderDescription": obj.get("sEzsignfolderDescription"),
            "eEzsignfolderStep": obj.get("eEzsignfolderStep"),
            "dtCreatedDate": obj.get("dtCreatedDate"),
            "dtEzsignfolderSentdate": obj.get("dtEzsignfolderSentdate"),
            "dtEzsignfolderDuedate": obj.get("dtEzsignfolderDuedate"),
            "iEzsigndocument": obj.get("iEzsigndocument"),
            "iEzsigndocumentEdm": obj.get("iEzsigndocumentEdm"),
            "iEzsignsignature": obj.get("iEzsignsignature"),
            "iEzsignsignatureSigned": obj.get("iEzsignsignatureSigned")
        })
        return _obj


