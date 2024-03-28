# UsergroupmembershipRequest

A Usergroupmembership Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroupmembership_id** | **int** | The unique ID of the Usergroupmembership | [optional] 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_usergroupexternal_id** | **int** | The unique ID of the Usergroupexternal | [optional] 

## Example

```python
from eZmaxApi.models.usergroupmembership_request import UsergroupmembershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupmembershipRequest from a JSON string
usergroupmembership_request_instance = UsergroupmembershipRequest.from_json(json)
# print the JSON string representation of the object
print(UsergroupmembershipRequest.to_json())

# convert the object into a dict
usergroupmembership_request_dict = usergroupmembership_request_instance.to_dict()
# create an instance of UsergroupmembershipRequest from a dict
usergroupmembership_request_form_dict = usergroupmembership_request.from_dict(usergroupmembership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


