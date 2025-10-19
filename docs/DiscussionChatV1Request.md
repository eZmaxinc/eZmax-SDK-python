# DiscussionChatV1Request

Request for POST /1/object/discussion/chat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_discussion_id** | **int** | The unique ID of the Discussion | [optional] 
**e_discussion_robot** | [**FieldEDiscussionRobot**](FieldEDiscussionRobot.md) |  | 
**t_discussion_message** | **str** | The Message of the Discussion | 

## Example

```python
from eZmaxApi.models.discussion_chat_v1_request import DiscussionChatV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionChatV1Request from a JSON string
discussion_chat_v1_request_instance = DiscussionChatV1Request.from_json(json)
# print the JSON string representation of the object
print(DiscussionChatV1Request.to_json())

# convert the object into a dict
discussion_chat_v1_request_dict = discussion_chat_v1_request_instance.to_dict()
# create an instance of DiscussionChatV1Request from a dict
discussion_chat_v1_request_from_dict = DiscussionChatV1Request.from_dict(discussion_chat_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


