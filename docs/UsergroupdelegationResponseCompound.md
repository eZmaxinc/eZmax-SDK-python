# UsergroupdelegationResponseCompound

A Usergroupdelegation Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroupdelegation_id** | **int** | The unique ID of the Usergroupdelegation | 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | 
**fki_user_id** | **int** | The unique ID of the User | 
**s_user_firstname** | **str** | The first name of the user | 
**s_user_lastname** | **str** | The last name of the user | 
**s_user_loginname** | **str** | The login name of the User. | 
**s_email_address** | **str** | The email address. | [optional] 
**s_usergroup_name_x** | **str** | The Name of the Usergroup in the language of the requester | 

## Example

```python
from eZmaxApi.models.usergroupdelegation_response_compound import UsergroupdelegationResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupdelegationResponseCompound from a JSON string
usergroupdelegation_response_compound_instance = UsergroupdelegationResponseCompound.from_json(json)
# print the JSON string representation of the object
print(UsergroupdelegationResponseCompound.to_json())

# convert the object into a dict
usergroupdelegation_response_compound_dict = usergroupdelegation_response_compound_instance.to_dict()
# create an instance of UsergroupdelegationResponseCompound from a dict
usergroupdelegation_response_compound_from_dict = UsergroupdelegationResponseCompound.from_dict(usergroupdelegation_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


