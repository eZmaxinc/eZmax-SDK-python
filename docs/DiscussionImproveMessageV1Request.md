# DiscussionImproveMessageV1Request

Request for POST /1/object/discussion/improveMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t_discussion_message** | **str** | The Message of the Discussion | 

## Example

```python
from eZmaxApi.models.discussion_improve_message_v1_request import DiscussionImproveMessageV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionImproveMessageV1Request from a JSON string
discussion_improve_message_v1_request_instance = DiscussionImproveMessageV1Request.from_json(json)
# print the JSON string representation of the object
print(DiscussionImproveMessageV1Request.to_json())

# convert the object into a dict
discussion_improve_message_v1_request_dict = discussion_improve_message_v1_request_instance.to_dict()
# create an instance of DiscussionImproveMessageV1Request from a dict
discussion_improve_message_v1_request_from_dict = DiscussionImproveMessageV1Request.from_dict(discussion_improve_message_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


