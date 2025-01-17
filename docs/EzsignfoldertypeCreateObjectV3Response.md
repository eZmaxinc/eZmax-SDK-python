# EzsignfoldertypeCreateObjectV3Response

Response for POST /3/object/ezsignfoldertype

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfoldertypeCreateObjectV3ResponseMPayload**](EzsignfoldertypeCreateObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_create_object_v3_response import EzsignfoldertypeCreateObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeCreateObjectV3Response from a JSON string
ezsignfoldertype_create_object_v3_response_instance = EzsignfoldertypeCreateObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeCreateObjectV3Response.to_json())

# convert the object into a dict
ezsignfoldertype_create_object_v3_response_dict = ezsignfoldertype_create_object_v3_response_instance.to_dict()
# create an instance of EzsignfoldertypeCreateObjectV3Response from a dict
ezsignfoldertype_create_object_v3_response_from_dict = EzsignfoldertypeCreateObjectV3Response.from_dict(ezsignfoldertype_create_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


