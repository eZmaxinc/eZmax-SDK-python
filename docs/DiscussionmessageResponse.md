# DiscussionmessageResponse

A Discussionmessage Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_discussionmessage_id** | **int** | The unique ID of the Discussionmessage | 
**fki_discussion_id** | **int** | The unique ID of the Discussion | 
**fki_discussionmembership_id** | **int** | The unique ID of the Discussionmembership | [optional] 
**fki_discussionmembership_id_actionrequired** | **int** | The unique ID of the Discussionmembership | [optional] 
**e_discussionmessage_status** | [**FieldEDiscussionmessageStatus**](FieldEDiscussionmessageStatus.md) |  | 
**t_discussionmessage_content** | **str** | The content of the Discussionmessage | 
**s_discussionmessage_creatorname** | **str** | The name the creator of the Discussionmessage. | 
**s_discussionmessage_actionrequiredname** | **str** | The name the Actionrequired of the Discussionmessage. | [optional] 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 

## Example

```python
from eZmaxApi.models.discussionmessage_response import DiscussionmessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionmessageResponse from a JSON string
discussionmessage_response_instance = DiscussionmessageResponse.from_json(json)
# print the JSON string representation of the object
print(DiscussionmessageResponse.to_json())

# convert the object into a dict
discussionmessage_response_dict = discussionmessage_response_instance.to_dict()
# create an instance of DiscussionmessageResponse from a dict
discussionmessage_response_from_dict = DiscussionmessageResponse.from_dict(discussionmessage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


