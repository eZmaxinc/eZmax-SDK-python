# DiscussionmembershipResponse

A Discussionmembership Object

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
from eZmaxApi.models.discussionmembership_response import DiscussionmembershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionmembershipResponse from a JSON string
discussionmembership_response_instance = DiscussionmembershipResponse.from_json(json)
# print the JSON string representation of the object
print(DiscussionmembershipResponse.to_json())

# convert the object into a dict
discussionmembership_response_dict = discussionmembership_response_instance.to_dict()
# create an instance of DiscussionmembershipResponse from a dict
discussionmembership_response_from_dict = DiscussionmembershipResponse.from_dict(discussionmembership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


