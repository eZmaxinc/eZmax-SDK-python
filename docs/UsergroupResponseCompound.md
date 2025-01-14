# UsergroupResponseCompound

A Usergroup Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroup_id** | **int** | The unique ID of the Usergroup | 
**obj_usergroup_name** | [**MultilingualUsergroupName**](MultilingualUsergroupName.md) |  | 
**s_usergroup_name_x** | **str** | The Name of the Usergroup in the language of the requester | [optional] 
**obj_email** | [**EmailRequest**](EmailRequest.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.usergroup_response_compound import UsergroupResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupResponseCompound from a JSON string
usergroup_response_compound_instance = UsergroupResponseCompound.from_json(json)
# print the JSON string representation of the object
print(UsergroupResponseCompound.to_json())

# convert the object into a dict
usergroup_response_compound_dict = usergroup_response_compound_instance.to_dict()
# create an instance of UsergroupResponseCompound from a dict
usergroup_response_compound_from_dict = UsergroupResponseCompound.from_dict(usergroup_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


