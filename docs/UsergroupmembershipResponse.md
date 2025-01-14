# UsergroupmembershipResponse

A Usergroupmembership Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroupmembership_id** | **int** | The unique ID of the Usergroupmembership | 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_usergroupexternal_id** | **int** | The unique ID of the Usergroupexternal | [optional] 
**s_user_firstname** | **str** | The first name of the user | [optional] 
**s_user_lastname** | **str** | The last name of the user | [optional] 
**s_user_loginname** | **str** | The login name of the User. | [optional] 
**s_email_address** | **str** | The email address. | [optional] 
**s_usergroup_name_x** | **str** | The Name of the Usergroup in the language of the requester | 
**s_usergroupexternal_name** | **str** | The name of the Usergroupexternal | [optional] 

## Example

```python
from eZmaxApi.models.usergroupmembership_response import UsergroupmembershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupmembershipResponse from a JSON string
usergroupmembership_response_instance = UsergroupmembershipResponse.from_json(json)
# print the JSON string representation of the object
print(UsergroupmembershipResponse.to_json())

# convert the object into a dict
usergroupmembership_response_dict = usergroupmembership_response_instance.to_dict()
# create an instance of UsergroupmembershipResponse from a dict
usergroupmembership_response_from_dict = UsergroupmembershipResponse.from_dict(usergroupmembership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


