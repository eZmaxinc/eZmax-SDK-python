# EzsigndocumentCreateObjectV1Response

Response for POST /1/object/ezsigndocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigndocumentCreateObjectV1ResponseMPayload**](EzsigndocumentCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_create_object_v1_response import EzsigndocumentCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentCreateObjectV1Response from a JSON string
ezsigndocument_create_object_v1_response_instance = EzsigndocumentCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print EzsigndocumentCreateObjectV1Response.to_json()

# convert the object into a dict
ezsigndocument_create_object_v1_response_dict = ezsigndocument_create_object_v1_response_instance.to_dict()
# create an instance of EzsigndocumentCreateObjectV1Response from a dict
ezsigndocument_create_object_v1_response_form_dict = ezsigndocument_create_object_v1_response.from_dict(ezsigndocument_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


