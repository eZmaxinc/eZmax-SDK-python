# EzsignfolderGetObjectV1Response

Response for GET /1/object/ezsignfolder/{pkiEzsignfolderID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfolderGetObjectV1ResponseMPayload**](EzsignfolderGetObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_object_v1_response import EzsignfolderGetObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetObjectV1Response from a JSON string
ezsignfolder_get_object_v1_response_instance = EzsignfolderGetObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetObjectV1Response.to_json())

# convert the object into a dict
ezsignfolder_get_object_v1_response_dict = ezsignfolder_get_object_v1_response_instance.to_dict()
# create an instance of EzsignfolderGetObjectV1Response from a dict
ezsignfolder_get_object_v1_response_from_dict = EzsignfolderGetObjectV1Response.from_dict(ezsignfolder_get_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


