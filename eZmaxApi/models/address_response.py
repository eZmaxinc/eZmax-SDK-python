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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class AddressResponse(BaseModel):
    """
    An Address Object
    """ # noqa: E501
    pki_address_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Address", alias="pkiAddressID")
    fki_addresstype_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Addresstype.  Valid values:  |Value|Description| |-|-| |1|Office| |2|Home| |3|Real Estate Invoice| |4|Invoicing| |5|Shipping|", alias="fkiAddresstypeID")
    s_address_civic: StrictStr = Field(description="The Civic number.", alias="sAddressCivic")
    s_address_street: StrictStr = Field(description="The Street Name", alias="sAddressStreet")
    s_address_suite: Optional[StrictStr] = Field(default=None, description="The Suite or appartment number", alias="sAddressSuite")
    s_address_city: StrictStr = Field(description="The City name", alias="sAddressCity")
    fki_province_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Province.  Here are some common values (Complete list must be retrieved from API):  |Value|Description| |-|-| |1|(Canada) Alberta |2|(Canada) British Columbia| |3|(Canada) Manitoba| |3|(Canada) Manitoba| |4|(Canada) New Brunswick| |5|(Canada) Newfoundland| |6|(Canada) Northwest Territories| |7|(Canada) Nova Scotia| |8|(Canada) Nunavut| |9|(Canada) Ontario| |10|(Canada) Prince Edward Island| |11|(Canada) Quebec| |12|(Canada) Saskatchewan| |13|(Canada) Yukon| |14|(United-States) Alabama| |15|(United-States) Alaska| |16|(United-States) Arizona| |17|(United-States) Arkansas| |18|(United-States) California| |19|(United-States) Colorado| |20|(United-States) Connecticut| |21|(United-States) Delaware| |22|(United-States) District of Columbia| |23|(United-States) Florida| |24|(United-States) Georgia| |25|(United-States) Hawaii| |26|(United-States) Idaho| |27|(United-States) Illinois| |28|(United-States) Indiana| |29|(United-States) Iowa| |30|(United-States) Kansas| |31|(United-States) Kentucky| |32|(United-States) Louisiane| |33|(United-States) Maine| |34|(United-States) Maryland| |35|(United-States) Massachusetts| |36|(United-States) Michigan| |37|(United-States) Minnesota| |38|(United-States) Mississippi| |39|(United-States) Missouri| |40|(United-States) Montana| |41|(United-States) Nebraska| |42|(United-States) Nevada| |43|(United-States) New Hampshire| |44|(United-States) New Jersey| |45|(United-States) New Mexico| |46|(United-States) New York| |47|(United-States) North Carolina| |48|(United-States) North Dakota| |49|(United-States) Ohio| |50|(United-States) Oklahoma| |51|(United-States) Oregon| |52|(United-States) Pennsylvania| |53|(United-States) Rhode Island| |54|(United-States) South Carolina| |55|(United-States) South Dakota| |56|(United-States) Tennessee| |57|(United-States) Texas| |58|(United-States) Utah| |60|(United-States) Vermont| |59|(United-States) Virginia| |61|(United-States) Washington| |62|(United-States) West Virginia| |63|(United-States) Wisconsin| |64|(United-States) Wyoming|", alias="fkiProvinceID")
    s_province_name_x: Annotated[str, Field(strict=True)] = Field(description="The name of the Province in the language of the requester", alias="sProvinceNameX")
    fki_country_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the Country.  Here are some common values (Complete list must be retrieved from API):  |Value|Description| |-|-| |1|Canada| |2|United-States|", alias="fkiCountryID")
    s_country_name_x: Annotated[str, Field(strict=True)] = Field(description="The name of the Country in the language of the requester", alias="sCountryNameX")
    s_address_zip: StrictStr = Field(description="The Postal/Zip Code  The value must be entered without spaces", alias="sAddressZip")
    f_address_longitude: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The Longitude of the Address", alias="fAddressLongitude")
    f_address_latitude: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The Latitude of the Address", alias="fAddressLatitude")
    __properties: ClassVar[List[str]] = ["pkiAddressID", "fkiAddresstypeID", "sAddressCivic", "sAddressStreet", "sAddressSuite", "sAddressCity", "fkiProvinceID", "sProvinceNameX", "fkiCountryID", "sCountryNameX", "sAddressZip", "fAddressLongitude", "fAddressLatitude"]

    @field_validator('s_province_name_x')
    def s_province_name_x_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
        return value

    @field_validator('s_country_name_x')
    def s_country_name_x_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^.{0,40}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,40}$/")
        return value

    @field_validator('f_address_longitude')
    def f_address_longitude_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(-?)(180(\.0{1,15})?|((1[0-7]\d)|(\d{1,2}))(\.\d{1,15})?)$", value):
            raise ValueError(r"must validate the regular expression /^(-?)(180(\.0{1,15})?|((1[0-7]\d)|(\d{1,2}))(\.\d{1,15})?)$/")
        return value

    @field_validator('f_address_latitude')
    def f_address_latitude_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(-?)(90(\.0{1,15})?|([1-8]?\d(\.\d{1,15})?))$", value):
            raise ValueError(r"must validate the regular expression /^(-?)(90(\.0{1,15})?|([1-8]?\d(\.\d{1,15})?))$/")
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
        """Create an instance of AddressResponse from a JSON string"""
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
        """Create an instance of AddressResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiAddressID": obj.get("pkiAddressID"),
            "fkiAddresstypeID": obj.get("fkiAddresstypeID"),
            "sAddressCivic": obj.get("sAddressCivic"),
            "sAddressStreet": obj.get("sAddressStreet"),
            "sAddressSuite": obj.get("sAddressSuite"),
            "sAddressCity": obj.get("sAddressCity"),
            "fkiProvinceID": obj.get("fkiProvinceID"),
            "sProvinceNameX": obj.get("sProvinceNameX"),
            "fkiCountryID": obj.get("fkiCountryID"),
            "sCountryNameX": obj.get("sCountryNameX"),
            "sAddressZip": obj.get("sAddressZip"),
            "fAddressLongitude": obj.get("fAddressLongitude"),
            "fAddressLatitude": obj.get("fAddressLatitude")
        })
        return _obj


