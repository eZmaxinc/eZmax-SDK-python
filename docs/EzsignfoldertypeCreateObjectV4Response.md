# EzsignfoldertypeCreateObjectV4Response

Response for POST /4/object/ezsignfoldertype

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfoldertypeCreateObjectV4ResponseMPayload**](EzsignfoldertypeCreateObjectV4ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_create_object_v4_response import EzsignfoldertypeCreateObjectV4Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeCreateObjectV4Response from a JSON string
ezsignfoldertype_create_object_v4_response_instance = EzsignfoldertypeCreateObjectV4Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeCreateObjectV4Response.to_json())

# convert the object into a dict
ezsignfoldertype_create_object_v4_response_dict = ezsignfoldertype_create_object_v4_response_instance.to_dict()
# create an instance of EzsignfoldertypeCreateObjectV4Response from a dict
ezsignfoldertype_create_object_v4_response_from_dict = EzsignfoldertypeCreateObjectV4Response.from_dict(ezsignfoldertype_create_object_v4_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


