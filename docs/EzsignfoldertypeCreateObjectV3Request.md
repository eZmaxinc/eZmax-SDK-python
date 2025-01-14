# EzsignfoldertypeCreateObjectV3Request

Request for POST /3/object/ezsignfoldertype

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignfoldertype** | [**List[EzsignfoldertypeRequestCompoundV3]**](EzsignfoldertypeRequestCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_create_object_v3_request import EzsignfoldertypeCreateObjectV3Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeCreateObjectV3Request from a JSON string
ezsignfoldertype_create_object_v3_request_instance = EzsignfoldertypeCreateObjectV3Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeCreateObjectV3Request.to_json())

# convert the object into a dict
ezsignfoldertype_create_object_v3_request_dict = ezsignfoldertype_create_object_v3_request_instance.to_dict()
# create an instance of EzsignfoldertypeCreateObjectV3Request from a dict
ezsignfoldertype_create_object_v3_request_from_dict = EzsignfoldertypeCreateObjectV3Request.from_dict(ezsignfoldertype_create_object_v3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


