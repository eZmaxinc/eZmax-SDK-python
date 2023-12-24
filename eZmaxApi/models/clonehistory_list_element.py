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
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ClonehistoryListElement(BaseModel):
    """
    A Clonehistory List Element
    """ # noqa: E501
    pki_clonehistory_id: Annotated[int, Field(le=16777215, strict=True, ge=1)] = Field(description="The unique ID of the Clonehistory", alias="pkiClonehistoryID")
    fki_user_id_cloning: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the User", alias="fkiUserIDCloning")
    fki_user_id_cloned: Annotated[int, Field(strict=True, ge=0)] = Field(description="The unique ID of the User", alias="fkiUserIDCloned")
    dt_clonehistory_firsthit: Annotated[str, Field(strict=True)] = Field(description="The firsthit of the Clonehistory", alias="dtClonehistoryFirsthit")
    dt_clonehistory_lasthit: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The lasthit of the Clonehistory", alias="dtClonehistoryLasthit")
    s_user_loginname_cloning: Annotated[str, Field(strict=True)] = Field(description="The login name of the User.", alias="sUserLoginnameCloning")
    s_user_firstname_cloning: StrictStr = Field(description="The first name of the user", alias="sUserFirstnameCloning")
    s_user_lastname_cloning: StrictStr = Field(description="The last name of the user", alias="sUserLastnameCloning")
    s_user_loginname_cloned: Annotated[str, Field(strict=True)] = Field(description="The login name of the User.", alias="sUserLoginnameCloned")
    s_user_firstname_cloned: StrictStr = Field(description="The first name of the user", alias="sUserFirstnameCloned")
    s_user_lastname_cloned: StrictStr = Field(description="The last name of the user", alias="sUserLastnameCloned")
    __properties: ClassVar[List[str]] = ["pkiClonehistoryID", "fkiUserIDCloning", "fkiUserIDCloned", "dtClonehistoryFirsthit", "dtClonehistoryLasthit", "sUserLoginnameCloning", "sUserFirstnameCloning", "sUserLastnameCloning", "sUserLoginnameCloned", "sUserFirstnameCloned", "sUserLastnameCloned"]

    @field_validator('dt_clonehistory_firsthit')
    def dt_clonehistory_firsthit_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$/")
        return value

    @field_validator('dt_clonehistory_lasthit')
    def dt_clonehistory_lasthit_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$/")
        return value

    @field_validator('s_user_loginname_cloning')
    def s_user_loginname_cloning_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(?:([\w\.-]+@[\w\.-]+\.\w{2,20})|([a-zA-Z0-9]){1,32})$", value):
            raise ValueError(r"must validate the regular expression /^(?:([\w\.-]+@[\w\.-]+\.\w{2,20})|([a-zA-Z0-9]){1,32})$/")
        return value

    @field_validator('s_user_loginname_cloned')
    def s_user_loginname_cloned_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(?:([\w\.-]+@[\w\.-]+\.\w{2,20})|([a-zA-Z0-9]){1,32})$", value):
            raise ValueError(r"must validate the regular expression /^(?:([\w\.-]+@[\w\.-]+\.\w{2,20})|([a-zA-Z0-9]){1,32})$/")
        return value

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
        """Create an instance of ClonehistoryListElement from a JSON string"""
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
        """Create an instance of ClonehistoryListElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkiClonehistoryID": obj.get("pkiClonehistoryID"),
            "fkiUserIDCloning": obj.get("fkiUserIDCloning"),
            "fkiUserIDCloned": obj.get("fkiUserIDCloned"),
            "dtClonehistoryFirsthit": obj.get("dtClonehistoryFirsthit"),
            "dtClonehistoryLasthit": obj.get("dtClonehistoryLasthit"),
            "sUserLoginnameCloning": obj.get("sUserLoginnameCloning"),
            "sUserFirstnameCloning": obj.get("sUserFirstnameCloning"),
            "sUserLastnameCloning": obj.get("sUserLastnameCloning"),
            "sUserLoginnameCloned": obj.get("sUserLoginnameCloned"),
            "sUserFirstnameCloned": obj.get("sUserFirstnameCloned"),
            "sUserLastnameCloned": obj.get("sUserLastnameCloned")
        })
        return _obj


