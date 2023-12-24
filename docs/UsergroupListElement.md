# UsergroupListElement

A Usergroup List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroup_id** | **int** | The unique ID of the Usergroup | 
**s_usergroup_name_x** | **str** | The Name of the Usergroup in the language of the requester | 
**i_count_user** | **int** | Number of users in group | 

## Example

```python
from eZmaxApi.models.usergroup_list_element import UsergroupListElement

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupListElement from a JSON string
usergroup_list_element_instance = UsergroupListElement.from_json(json)
# print the JSON string representation of the object
print UsergroupListElement.to_json()

# convert the object into a dict
usergroup_list_element_dict = usergroup_list_element_instance.to_dict()
# create an instance of UsergroupListElement from a dict
usergroup_list_element_form_dict = usergroup_list_element.from_dict(usergroup_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


