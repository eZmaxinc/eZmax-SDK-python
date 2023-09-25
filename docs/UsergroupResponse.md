# UsergroupResponse

A Usergroup Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroup_id** | **int** | The unique ID of the Usergroup | 
**obj_usergroup_name** | [**MultilingualUsergroupName**](MultilingualUsergroupName.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_response import UsergroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupResponse from a JSON string
usergroup_response_instance = UsergroupResponse.from_json(json)
# print the JSON string representation of the object
print UsergroupResponse.to_json()

# convert the object into a dict
usergroup_response_dict = usergroup_response_instance.to_dict()
# create an instance of UsergroupResponse from a dict
usergroup_response_form_dict = usergroup_response.from_dict(usergroup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


