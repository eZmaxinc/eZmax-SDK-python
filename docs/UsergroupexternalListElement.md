# UsergroupexternalListElement

A Usergroupexternal List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroupexternal_id** | **int** | The unique ID of the Usergroupexternal | 
**s_usergroupexternal_name** | **str** | The name of the Usergroupexternal | 
**s_usergroupexternal_id** | **str** | The id of the Usergroupexternal | 

## Example

```python
from eZmaxApi.models.usergroupexternal_list_element import UsergroupexternalListElement

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalListElement from a JSON string
usergroupexternal_list_element_instance = UsergroupexternalListElement.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalListElement.to_json())

# convert the object into a dict
usergroupexternal_list_element_dict = usergroupexternal_list_element_instance.to_dict()
# create an instance of UsergroupexternalListElement from a dict
usergroupexternal_list_element_from_dict = UsergroupexternalListElement.from_dict(usergroupexternal_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


