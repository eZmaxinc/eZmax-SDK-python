# DiscussionmembershipResponseCompound

A Discussionmembership Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_discussionmembership_id** | **int** | The unique ID of the Discussionmembership | 
**fki_discussion_id** | **int** | The unique ID of the Discussion | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | [optional] 
**fki_modulesection_id** | **int** | The unique ID of the Modulesection | [optional] 
**s_discussionmembership_description** | **str** | The Description containing the detail of who the Discussionmembership refers to | 
**dt_discussionmembership_joined** | **str** | The joined date of the Discussionmembership | 

## Example

```python
from eZmaxApi.models.discussionmembership_response_compound import DiscussionmembershipResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionmembershipResponseCompound from a JSON string
discussionmembership_response_compound_instance = DiscussionmembershipResponseCompound.from_json(json)
# print the JSON string representation of the object
print(DiscussionmembershipResponseCompound.to_json())

# convert the object into a dict
discussionmembership_response_compound_dict = discussionmembership_response_compound_instance.to_dict()
# create an instance of DiscussionmembershipResponseCompound from a dict
discussionmembership_response_compound_from_dict = DiscussionmembershipResponseCompound.from_dict(discussionmembership_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


