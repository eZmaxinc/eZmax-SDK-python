# EzsignfolderCreateObjectV1Response

Response for POST /1/object/ezsignfolder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignfolderCreateObjectV1ResponseMPayload**](EzsignfolderCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_create_object_v1_response import EzsignfolderCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderCreateObjectV1Response from a JSON string
ezsignfolder_create_object_v1_response_instance = EzsignfolderCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderCreateObjectV1Response.to_json())

# convert the object into a dict
ezsignfolder_create_object_v1_response_dict = ezsignfolder_create_object_v1_response_instance.to_dict()
# create an instance of EzsignfolderCreateObjectV1Response from a dict
ezsignfolder_create_object_v1_response_from_dict = EzsignfolderCreateObjectV1Response.from_dict(ezsignfolder_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


