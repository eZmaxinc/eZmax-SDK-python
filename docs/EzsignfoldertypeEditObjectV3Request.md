# EzsignfoldertypeEditObjectV3Request

Request for PUT /3/object/ezsignfoldertype/{pkiEzsignfoldertypeID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfoldertype** | [**EzsignfoldertypeRequestCompoundV3**](EzsignfoldertypeRequestCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_edit_object_v3_request import EzsignfoldertypeEditObjectV3Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeEditObjectV3Request from a JSON string
ezsignfoldertype_edit_object_v3_request_instance = EzsignfoldertypeEditObjectV3Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeEditObjectV3Request.to_json())

# convert the object into a dict
ezsignfoldertype_edit_object_v3_request_dict = ezsignfoldertype_edit_object_v3_request_instance.to_dict()
# create an instance of EzsignfoldertypeEditObjectV3Request from a dict
ezsignfoldertype_edit_object_v3_request_from_dict = EzsignfoldertypeEditObjectV3Request.from_dict(ezsignfoldertype_edit_object_v3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


