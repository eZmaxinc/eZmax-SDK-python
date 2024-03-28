# MultilingualUsergroupName

The name of the Usergroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_usergroup_name1** | **str** | The name of the Usergroup in French | [optional] 
**s_usergroup_name2** | **str** | The name of the Usergroup in English | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_usergroup_name import MultilingualUsergroupName

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualUsergroupName from a JSON string
multilingual_usergroup_name_instance = MultilingualUsergroupName.from_json(json)
# print the JSON string representation of the object
print(MultilingualUsergroupName.to_json())

# convert the object into a dict
multilingual_usergroup_name_dict = multilingual_usergroup_name_instance.to_dict()
# create an instance of MultilingualUsergroupName from a dict
multilingual_usergroup_name_form_dict = multilingual_usergroup_name.from_dict(multilingual_usergroup_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


