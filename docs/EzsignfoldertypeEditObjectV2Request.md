# EzsignfoldertypeEditObjectV2Request

Request for PUT /2/object/ezsignfoldertype/{pkiEzsignfoldertypeID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfoldertype** | [**EzsignfoldertypeRequestCompoundV2**](EzsignfoldertypeRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_edit_object_v2_request import EzsignfoldertypeEditObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeEditObjectV2Request from a JSON string
ezsignfoldertype_edit_object_v2_request_instance = EzsignfoldertypeEditObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeEditObjectV2Request.to_json())

# convert the object into a dict
ezsignfoldertype_edit_object_v2_request_dict = ezsignfoldertype_edit_object_v2_request_instance.to_dict()
# create an instance of EzsignfoldertypeEditObjectV2Request from a dict
ezsignfoldertype_edit_object_v2_request_form_dict = ezsignfoldertype_edit_object_v2_request.from_dict(ezsignfoldertype_edit_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


