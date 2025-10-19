# EzsignsignatureGetObjectV4Response

Response for GET /4/object/ezsignsignature/{pkiEzsignsignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignsignatureGetObjectV4ResponseMPayload**](EzsignsignatureGetObjectV4ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_get_object_v4_response import EzsignsignatureGetObjectV4Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureGetObjectV4Response from a JSON string
ezsignsignature_get_object_v4_response_instance = EzsignsignatureGetObjectV4Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureGetObjectV4Response.to_json())

# convert the object into a dict
ezsignsignature_get_object_v4_response_dict = ezsignsignature_get_object_v4_response_instance.to_dict()
# create an instance of EzsignsignatureGetObjectV4Response from a dict
ezsignsignature_get_object_v4_response_from_dict = EzsignsignatureGetObjectV4Response.from_dict(ezsignsignature_get_object_v4_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


