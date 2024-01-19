# DiscussionmembershipRequest

A Discussionmembership Object

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
from eZmaxApi.models.discussionmembership_request import DiscussionmembershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionmembershipRequest from a JSON string
discussionmembership_request_instance = DiscussionmembershipRequest.from_json(json)
# print the JSON string representation of the object
print DiscussionmembershipRequest.to_json()

# convert the object into a dict
discussionmembership_request_dict = discussionmembership_request_instance.to_dict()
# create an instance of DiscussionmembershipRequest from a dict
discussionmembership_request_form_dict = discussionmembership_request.from_dict(discussionmembership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


