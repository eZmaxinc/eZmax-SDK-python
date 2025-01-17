# EzsignfolderCreateObjectV2Response

Response for POST /2/object/ezsignfolder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignfolderCreateObjectV2ResponseMPayload**](EzsignfolderCreateObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_create_object_v2_response import EzsignfolderCreateObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderCreateObjectV2Response from a JSON string
ezsignfolder_create_object_v2_response_instance = EzsignfolderCreateObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderCreateObjectV2Response.to_json())

# convert the object into a dict
ezsignfolder_create_object_v2_response_dict = ezsignfolder_create_object_v2_response_instance.to_dict()
# create an instance of EzsignfolderCreateObjectV2Response from a dict
ezsignfolder_create_object_v2_response_from_dict = EzsignfolderCreateObjectV2Response.from_dict(ezsignfolder_create_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


