# EzsigndiscussionCreateObjectV1Response

Response for POST /1/object/ezsigndiscussion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigndiscussionCreateObjectV1ResponseMPayload**](EzsigndiscussionCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndiscussion_create_object_v1_response import EzsigndiscussionCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndiscussionCreateObjectV1Response from a JSON string
ezsigndiscussion_create_object_v1_response_instance = EzsigndiscussionCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print EzsigndiscussionCreateObjectV1Response.to_json()

# convert the object into a dict
ezsigndiscussion_create_object_v1_response_dict = ezsigndiscussion_create_object_v1_response_instance.to_dict()
# create an instance of EzsigndiscussionCreateObjectV1Response from a dict
ezsigndiscussion_create_object_v1_response_form_dict = ezsigndiscussion_create_object_v1_response.from_dict(ezsigndiscussion_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


