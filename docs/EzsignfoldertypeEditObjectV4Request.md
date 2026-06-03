# EzsignfoldertypeEditObjectV4Request

Request for PUT /4/object/ezsignfoldertype/{pkiEzsignfoldertypeID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfoldertype** | [**EzsignfoldertypeRequestCompoundV4**](EzsignfoldertypeRequestCompoundV4.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_edit_object_v4_request import EzsignfoldertypeEditObjectV4Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeEditObjectV4Request from a JSON string
ezsignfoldertype_edit_object_v4_request_instance = EzsignfoldertypeEditObjectV4Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeEditObjectV4Request.to_json())

# convert the object into a dict
ezsignfoldertype_edit_object_v4_request_dict = ezsignfoldertype_edit_object_v4_request_instance.to_dict()
# create an instance of EzsignfoldertypeEditObjectV4Request from a dict
ezsignfoldertype_edit_object_v4_request_from_dict = EzsignfoldertypeEditObjectV4Request.from_dict(ezsignfoldertype_edit_object_v4_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


