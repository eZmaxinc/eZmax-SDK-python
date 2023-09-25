# PermissionResponseCompound

A Permission Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_permission_id** | **int** | The unique ID of the Permission | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_apikey_id** | **int** | The unique ID of the Apikey | [optional] 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | [optional] 
**fki_company_id** | **int** | The unique ID of the Company | [optional] 
**fki_modulesection_id** | **int** | The unique ID of the Modulesection | 
**s_company_name_x** | **str** | The Name of the Company in the language of the requester | [optional] 

## Example

```python
from eZmaxApi.models.permission_response_compound import PermissionResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionResponseCompound from a JSON string
permission_response_compound_instance = PermissionResponseCompound.from_json(json)
# print the JSON string representation of the object
print PermissionResponseCompound.to_json()

# convert the object into a dict
permission_response_compound_dict = permission_response_compound_instance.to_dict()
# create an instance of PermissionResponseCompound from a dict
permission_response_compound_form_dict = permission_response_compound.from_dict(permission_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


