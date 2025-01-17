# EzsignfolderCreateObjectV3Response

Response for POST /3/object/ezsignfolder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfolderCreateObjectV3ResponseMPayload**](EzsignfolderCreateObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_create_object_v3_response import EzsignfolderCreateObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderCreateObjectV3Response from a JSON string
ezsignfolder_create_object_v3_response_instance = EzsignfolderCreateObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderCreateObjectV3Response.to_json())

# convert the object into a dict
ezsignfolder_create_object_v3_response_dict = ezsignfolder_create_object_v3_response_instance.to_dict()
# create an instance of EzsignfolderCreateObjectV3Response from a dict
ezsignfolder_create_object_v3_response_from_dict = EzsignfolderCreateObjectV3Response.from_dict(ezsignfolder_create_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


