# EzsignfoldertypeEditObjectV1Request

Request for PUT /1/object/ezsignfoldertype/{pkiEzsignfoldertypeID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfoldertype** | [**EzsignfoldertypeRequestCompound**](EzsignfoldertypeRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_edit_object_v1_request import EzsignfoldertypeEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeEditObjectV1Request from a JSON string
ezsignfoldertype_edit_object_v1_request_instance = EzsignfoldertypeEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignfoldertypeEditObjectV1Request.to_json()

# convert the object into a dict
ezsignfoldertype_edit_object_v1_request_dict = ezsignfoldertype_edit_object_v1_request_instance.to_dict()
# create an instance of EzsignfoldertypeEditObjectV1Request from a dict
ezsignfoldertype_edit_object_v1_request_form_dict = ezsignfoldertype_edit_object_v1_request.from_dict(ezsignfoldertype_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


