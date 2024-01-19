# DiscussionmessageCreateObjectV1Response

Response for POST /1/object/discussionmessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DiscussionmessageCreateObjectV1ResponseMPayload**](DiscussionmessageCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.discussionmessage_create_object_v1_response import DiscussionmessageCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionmessageCreateObjectV1Response from a JSON string
discussionmessage_create_object_v1_response_instance = DiscussionmessageCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print DiscussionmessageCreateObjectV1Response.to_json()

# convert the object into a dict
discussionmessage_create_object_v1_response_dict = discussionmessage_create_object_v1_response_instance.to_dict()
# create an instance of DiscussionmessageCreateObjectV1Response from a dict
discussionmessage_create_object_v1_response_form_dict = discussionmessage_create_object_v1_response.from_dict(discussionmessage_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


