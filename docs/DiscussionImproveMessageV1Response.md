# DiscussionImproveMessageV1Response

Response for POST /1/object/discussion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DiscussionImproveMessageV1ResponseMPayload**](DiscussionImproveMessageV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.discussion_improve_message_v1_response import DiscussionImproveMessageV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionImproveMessageV1Response from a JSON string
discussion_improve_message_v1_response_instance = DiscussionImproveMessageV1Response.from_json(json)
# print the JSON string representation of the object
print(DiscussionImproveMessageV1Response.to_json())

# convert the object into a dict
discussion_improve_message_v1_response_dict = discussion_improve_message_v1_response_instance.to_dict()
# create an instance of DiscussionImproveMessageV1Response from a dict
discussion_improve_message_v1_response_from_dict = DiscussionImproveMessageV1Response.from_dict(discussion_improve_message_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


