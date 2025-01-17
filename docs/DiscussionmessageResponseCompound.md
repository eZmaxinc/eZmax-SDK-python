# DiscussionmessageResponseCompound

A Discussionmessage Object and children

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
from eZmaxApi.models.discussionmessage_response_compound import DiscussionmessageResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionmessageResponseCompound from a JSON string
discussionmessage_response_compound_instance = DiscussionmessageResponseCompound.from_json(json)
# print the JSON string representation of the object
print(DiscussionmessageResponseCompound.to_json())

# convert the object into a dict
discussionmessage_response_compound_dict = discussionmessage_response_compound_instance.to_dict()
# create an instance of DiscussionmessageResponseCompound from a dict
discussionmessage_response_compound_from_dict = DiscussionmessageResponseCompound.from_dict(discussionmessage_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


