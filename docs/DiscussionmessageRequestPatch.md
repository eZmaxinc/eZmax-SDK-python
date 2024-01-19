# DiscussionmessageRequestPatch

A Discussionmessage Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_discussionmembership_id_actionrequired** | **int** | The unique ID of the Discussionmembership | [optional] 
**t_discussionmessage_content** | **str** | The content of the Discussionmessage | [optional] 

## Example

```python
from eZmaxApi.models.discussionmessage_request_patch import DiscussionmessageRequestPatch

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionmessageRequestPatch from a JSON string
discussionmessage_request_patch_instance = DiscussionmessageRequestPatch.from_json(json)
# print the JSON string representation of the object
print DiscussionmessageRequestPatch.to_json()

# convert the object into a dict
discussionmessage_request_patch_dict = discussionmessage_request_patch_instance.to_dict()
# create an instance of DiscussionmessageRequestPatch from a dict
discussionmessage_request_patch_form_dict = discussionmessage_request_patch.from_dict(discussionmessage_request_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


