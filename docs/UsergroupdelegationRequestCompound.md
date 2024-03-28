# UsergroupdelegationRequestCompound

A Usergroupdelegation Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroupdelegation_id** | **int** | The unique ID of the Usergroupdelegation | [optional] 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | 
**fki_user_id** | **int** | The unique ID of the User | 

## Example

```python
from eZmaxApi.models.usergroupdelegation_request_compound import UsergroupdelegationRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupdelegationRequestCompound from a JSON string
usergroupdelegation_request_compound_instance = UsergroupdelegationRequestCompound.from_json(json)
# print the JSON string representation of the object
print(UsergroupdelegationRequestCompound.to_json())

# convert the object into a dict
usergroupdelegation_request_compound_dict = usergroupdelegation_request_compound_instance.to_dict()
# create an instance of UsergroupdelegationRequestCompound from a dict
usergroupdelegation_request_compound_form_dict = usergroupdelegation_request_compound.from_dict(usergroupdelegation_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


