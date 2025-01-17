# EzsigndocumentCreateObjectV3Response

Response for POST /3/object/ezsigndocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigndocumentCreateObjectV3ResponseMPayload**](EzsigndocumentCreateObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_create_object_v3_response import EzsigndocumentCreateObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentCreateObjectV3Response from a JSON string
ezsigndocument_create_object_v3_response_instance = EzsigndocumentCreateObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentCreateObjectV3Response.to_json())

# convert the object into a dict
ezsigndocument_create_object_v3_response_dict = ezsigndocument_create_object_v3_response_instance.to_dict()
# create an instance of EzsigndocumentCreateObjectV3Response from a dict
ezsigndocument_create_object_v3_response_from_dict = EzsigndocumentCreateObjectV3Response.from_dict(ezsigndocument_create_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


