# UsergroupdelegationRequest

A Usergroupdelegation Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroupdelegation_id** | **int** | The unique ID of the Usergroupdelegation | [optional] 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | 
**fki_user_id** | **int** | The unique ID of the User | 

## Example

```python
from eZmaxApi.models.usergroupdelegation_request import UsergroupdelegationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupdelegationRequest from a JSON string
usergroupdelegation_request_instance = UsergroupdelegationRequest.from_json(json)
# print the JSON string representation of the object
print(UsergroupdelegationRequest.to_json())

# convert the object into a dict
usergroupdelegation_request_dict = usergroupdelegation_request_instance.to_dict()
# create an instance of UsergroupdelegationRequest from a dict
usergroupdelegation_request_form_dict = usergroupdelegation_request.from_dict(usergroupdelegation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


