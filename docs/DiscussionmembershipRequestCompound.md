# DiscussionmembershipRequestCompound

A Discussionmembership Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_discussionmembership_id** | **int** | The unique ID of the Discussionmembership | [optional] 
**fki_discussion_id** | **int** | The unique ID of the Discussion | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | [optional] 
**fki_modulesection_id** | **int** | The unique ID of the Modulesection | [optional] 
**dt_discussionmembership_joined** | **str** | The joined date of the Discussionmembership | 

## Example

```python
from eZmaxApi.models.discussionmembership_request_compound import DiscussionmembershipRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionmembershipRequestCompound from a JSON string
discussionmembership_request_compound_instance = DiscussionmembershipRequestCompound.from_json(json)
# print the JSON string representation of the object
print DiscussionmembershipRequestCompound.to_json()

# convert the object into a dict
discussionmembership_request_compound_dict = discussionmembership_request_compound_instance.to_dict()
# create an instance of DiscussionmembershipRequestCompound from a dict
discussionmembership_request_compound_form_dict = discussionmembership_request_compound.from_dict(discussionmembership_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


