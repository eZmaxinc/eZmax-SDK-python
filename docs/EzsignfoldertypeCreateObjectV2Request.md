# EzsignfoldertypeCreateObjectV2Request

Request for POST /2/object/ezsignfoldertype

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignfoldertype** | [**List[EzsignfoldertypeRequestCompoundV2]**](EzsignfoldertypeRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_create_object_v2_request import EzsignfoldertypeCreateObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeCreateObjectV2Request from a JSON string
ezsignfoldertype_create_object_v2_request_instance = EzsignfoldertypeCreateObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeCreateObjectV2Request.to_json())

# convert the object into a dict
ezsignfoldertype_create_object_v2_request_dict = ezsignfoldertype_create_object_v2_request_instance.to_dict()
# create an instance of EzsignfoldertypeCreateObjectV2Request from a dict
ezsignfoldertype_create_object_v2_request_form_dict = ezsignfoldertype_create_object_v2_request.from_dict(ezsignfoldertype_create_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


