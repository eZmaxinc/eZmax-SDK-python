# EzsigndocumentCreateObjectV2Response

Response for POST /2/object/ezsigndocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigndocumentCreateObjectV2ResponseMPayload**](EzsigndocumentCreateObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_create_object_v2_response import EzsigndocumentCreateObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentCreateObjectV2Response from a JSON string
ezsigndocument_create_object_v2_response_instance = EzsigndocumentCreateObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentCreateObjectV2Response.to_json())

# convert the object into a dict
ezsigndocument_create_object_v2_response_dict = ezsigndocument_create_object_v2_response_instance.to_dict()
# create an instance of EzsigndocumentCreateObjectV2Response from a dict
ezsigndocument_create_object_v2_response_from_dict = EzsigndocumentCreateObjectV2Response.from_dict(ezsigndocument_create_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


