# EzsignfoldertypeCreateObjectV1Request

Request for POST /1/object/ezsignfoldertype

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignfoldertype** | [**List[EzsignfoldertypeRequestCompound]**](EzsignfoldertypeRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_create_object_v1_request import EzsignfoldertypeCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeCreateObjectV1Request from a JSON string
ezsignfoldertype_create_object_v1_request_instance = EzsignfoldertypeCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignfoldertypeCreateObjectV1Request.to_json()

# convert the object into a dict
ezsignfoldertype_create_object_v1_request_dict = ezsignfoldertype_create_object_v1_request_instance.to_dict()
# create an instance of EzsignfoldertypeCreateObjectV1Request from a dict
ezsignfoldertype_create_object_v1_request_form_dict = ezsignfoldertype_create_object_v1_request.from_dict(ezsignfoldertype_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


