# EzsignfolderCreateObjectV3Request

Request for POST /3/object/ezsignfolder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignfolder** | [**List[EzsignfolderRequestCompoundV3]**](EzsignfolderRequestV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_create_object_v3_request import EzsignfolderCreateObjectV3Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderCreateObjectV3Request from a JSON string
ezsignfolder_create_object_v3_request_instance = EzsignfolderCreateObjectV3Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderCreateObjectV3Request.to_json())

# convert the object into a dict
ezsignfolder_create_object_v3_request_dict = ezsignfolder_create_object_v3_request_instance.to_dict()
# create an instance of EzsignfolderCreateObjectV3Request from a dict
ezsignfolder_create_object_v3_request_from_dict = EzsignfolderCreateObjectV3Request.from_dict(ezsignfolder_create_object_v3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


