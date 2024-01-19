# DiscussionCreateObjectV1Response

Response for POST /1/object/discussion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DiscussionCreateObjectV1ResponseMPayload**](DiscussionCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.discussion_create_object_v1_response import DiscussionCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionCreateObjectV1Response from a JSON string
discussion_create_object_v1_response_instance = DiscussionCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print DiscussionCreateObjectV1Response.to_json()

# convert the object into a dict
discussion_create_object_v1_response_dict = discussion_create_object_v1_response_instance.to_dict()
# create an instance of DiscussionCreateObjectV1Response from a dict
discussion_create_object_v1_response_form_dict = discussion_create_object_v1_response.from_dict(discussion_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


