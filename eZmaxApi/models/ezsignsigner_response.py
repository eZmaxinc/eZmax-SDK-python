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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, conint

class EzsignsignerResponse(BaseModel):
    """
    An Ezsignsigner Object  # noqa: E501
    """
    pki_ezsignsigner_id: conint(strict=True, ge=0) = Field(..., alias="pkiEzsignsignerID", description="The unique ID of the Ezsignsigner")
    fki_taxassignment_id: conint(strict=True, le=15, ge=0) = Field(..., alias="fkiTaxassignmentID", description="The unique ID of the Taxassignment.  Valid values:  |Value|Description| |-|-| |1|No tax| |2|GST| |3|HST (ON)| |4|HST (NB)| |5|HST (NS)| |6|HST (NL)| |7|HST (PE)| |8|GST + QST (QC)| |9|GST + QST (QC) Non-Recoverable| |10|GST + PST (BC)| |11|GST + PST (SK)| |12|GST + RST (MB)| |13|GST + PST (BC) Non-Recoverable| |14|GST + PST (SK) Non-Recoverable| |15|GST + RST (MB) Non-Recoverable|")
    fki_secretquestion_id: Optional[conint(strict=True, ge=0)] = Field(None, alias="fkiSecretquestionID", description="The unique ID of the Secretquestion.  Valid values:  |Value|Description| |-|-| |1|The name of the hospital in which you were born| |2|The name of your grade school| |3|The last name of your favorite teacher| |4|Your favorite sports team| |5|Your favorite TV show| |6|Your favorite movie| |7|The name of the street on which you grew up| |8|The name of your first employer| |9|Your first car| |10|Your favorite food| |11|The name of your first pet| |12|Favorite musician/band| |13|What instrument you play| |14|Your father's middle name| |15|Your mother's maiden name| |16|Name of your eldest child| |17|Your spouse's middle name| |18|Favorite restaurant| |19|Childhood nickname| |20|Favorite vacation destination| |21|Your boat's name| |22|Date of Birth (YYYY-MM-DD)|")
    fki_userlogintype_id: conint(strict=True, ge=0) = Field(..., alias="fkiUserlogintypeID", description="The unique ID of the Userlogintype  Valid values:  |Value|Description|Detail| |-|-|-| |1|**Email Only**|The Ezsignsigner will receive a secure link by email| |2|**Email and phone or SMS**|The Ezsignsigner will receive a secure link by email and will need to authenticate using SMS or Phone call. **Additional fee applies**| |3|**Email and secret question**|The Ezsignsigner will receive a secure link by email and will need to authenticate using a predefined question and answer| |4|**In person only**|The Ezsignsigner will only be able to sign \"In-Person\" and there won't be any authentication. No email will be sent for invitation to sign. Make sure you evaluate the risk of signature denial and at minimum, we recommend you use a handwritten signature type| |5|**In person with phone or SMS**|The Ezsignsigner will only be able to sign \"In-Person\" and will need to authenticate using SMS or Phone call. No email will be sent for invitation to sign. **Additional fee applies**|")
    s_userlogintype_description_x: StrictStr = Field(..., alias="sUserlogintypeDescriptionX", description="The description of the Userlogintype in the language of the requester")
    __properties = ["pkiEzsignsignerID", "fkiTaxassignmentID", "fkiSecretquestionID", "fkiUserlogintypeID", "sUserlogintypeDescriptionX"]

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
    def from_json(cls, json_str: str) -> EzsignsignerResponse:
        """Create an instance of EzsignsignerResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EzsignsignerResponse:
        """Create an instance of EzsignsignerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EzsignsignerResponse.parse_obj(obj)

        _obj = EzsignsignerResponse.parse_obj({
            "pki_ezsignsigner_id": obj.get("pkiEzsignsignerID"),
            "fki_taxassignment_id": obj.get("fkiTaxassignmentID"),
            "fki_secretquestion_id": obj.get("fkiSecretquestionID"),
            "fki_userlogintype_id": obj.get("fkiUserlogintypeID"),
            "s_userlogintype_description_x": obj.get("sUserlogintypeDescriptionX")
        })
        return _obj


