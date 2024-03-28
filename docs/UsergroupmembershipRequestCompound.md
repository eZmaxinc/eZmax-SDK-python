# UsergroupmembershipRequestCompound

A Usergroupmembership Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroupmembership_id** | **int** | The unique ID of the Usergroupmembership | [optional] 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_usergroupexternal_id** | **int** | The unique ID of the Usergroupexternal | [optional] 

## Example

```python
from eZmaxApi.models.usergroupmembership_request_compound import UsergroupmembershipRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupmembershipRequestCompound from a JSON string
usergroupmembership_request_compound_instance = UsergroupmembershipRequestCompound.from_json(json)
# print the JSON string representation of the object
print(UsergroupmembershipRequestCompound.to_json())

# convert the object into a dict
usergroupmembership_request_compound_dict = usergroupmembership_request_compound_instance.to_dict()
# create an instance of UsergroupmembershipRequestCompound from a dict
usergroupmembership_request_compound_form_dict = usergroupmembership_request_compound.from_dict(usergroupmembership_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


