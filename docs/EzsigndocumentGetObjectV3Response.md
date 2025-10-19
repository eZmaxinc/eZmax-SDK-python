# EzsigndocumentGetObjectV3Response

Response for GET /3/object/ezsigndocument/{pkiEzsigndocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigndocumentGetObjectV3ResponseMPayload**](EzsigndocumentGetObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_object_v3_response import EzsigndocumentGetObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetObjectV3Response from a JSON string
ezsigndocument_get_object_v3_response_instance = EzsigndocumentGetObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetObjectV3Response.to_json())

# convert the object into a dict
ezsigndocument_get_object_v3_response_dict = ezsigndocument_get_object_v3_response_instance.to_dict()
# create an instance of EzsigndocumentGetObjectV3Response from a dict
ezsigndocument_get_object_v3_response_from_dict = EzsigndocumentGetObjectV3Response.from_dict(ezsigndocument_get_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


