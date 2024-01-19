# DiscussionmessageRequest

A Discussionmessage Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_discussionmessage_id** | **int** | The unique ID of the Discussionmessage | [optional] 
**fki_discussion_id** | **int** | The unique ID of the Discussion | 
**fki_discussionmembership_id_actionrequired** | **int** | The unique ID of the Discussionmembership | [optional] 
**t_discussionmessage_content** | **str** | The content of the Discussionmessage | 

## Example

```python
from eZmaxApi.models.discussionmessage_request import DiscussionmessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionmessageRequest from a JSON string
discussionmessage_request_instance = DiscussionmessageRequest.from_json(json)
# print the JSON string representation of the object
print DiscussionmessageRequest.to_json()

# convert the object into a dict
discussionmessage_request_dict = discussionmessage_request_instance.to_dict()
# create an instance of DiscussionmessageRequest from a dict
discussionmessage_request_form_dict = discussionmessage_request.from_dict(discussionmessage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


