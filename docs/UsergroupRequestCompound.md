# UsergroupRequestCompound

A Usergroup Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroup_id** | **int** | The unique ID of the Usergroup | [optional] 
**obj_usergroup_name** | [**MultilingualUsergroupName**](MultilingualUsergroupName.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_request_compound import UsergroupRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupRequestCompound from a JSON string
usergroup_request_compound_instance = UsergroupRequestCompound.from_json(json)
# print the JSON string representation of the object
print UsergroupRequestCompound.to_json()

# convert the object into a dict
usergroup_request_compound_dict = usergroup_request_compound_instance.to_dict()
# create an instance of UsergroupRequestCompound from a dict
usergroup_request_compound_form_dict = usergroup_request_compound.from_dict(usergroup_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


