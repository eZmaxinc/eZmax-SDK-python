# DiscussionImproveMessageV1ResponseMPayload

Payload for POST /1/object/discussion/improveMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t_discussion_message** | **str** | The Message of the Discussion | 

## Example

```python
from eZmaxApi.models.discussion_improve_message_v1_response_m_payload import DiscussionImproveMessageV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionImproveMessageV1ResponseMPayload from a JSON string
discussion_improve_message_v1_response_m_payload_instance = DiscussionImproveMessageV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DiscussionImproveMessageV1ResponseMPayload.to_json())

# convert the object into a dict
discussion_improve_message_v1_response_m_payload_dict = discussion_improve_message_v1_response_m_payload_instance.to_dict()
# create an instance of DiscussionImproveMessageV1ResponseMPayload from a dict
discussion_improve_message_v1_response_m_payload_from_dict = DiscussionImproveMessageV1ResponseMPayload.from_dict(discussion_improve_message_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


