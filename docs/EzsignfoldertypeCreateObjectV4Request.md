# EzsignfoldertypeCreateObjectV4Request

Request for POST /4/object/ezsignfoldertype

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignfoldertype** | [**List[EzsignfoldertypeRequestCompoundV4]**](EzsignfoldertypeRequestCompoundV4.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_create_object_v4_request import EzsignfoldertypeCreateObjectV4Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeCreateObjectV4Request from a JSON string
ezsignfoldertype_create_object_v4_request_instance = EzsignfoldertypeCreateObjectV4Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeCreateObjectV4Request.to_json())

# convert the object into a dict
ezsignfoldertype_create_object_v4_request_dict = ezsignfoldertype_create_object_v4_request_instance.to_dict()
# create an instance of EzsignfoldertypeCreateObjectV4Request from a dict
ezsignfoldertype_create_object_v4_request_from_dict = EzsignfoldertypeCreateObjectV4Request.from_dict(ezsignfoldertype_create_object_v4_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


