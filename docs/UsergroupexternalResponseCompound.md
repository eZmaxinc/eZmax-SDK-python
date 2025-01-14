# UsergroupexternalResponseCompound

A Usergroupexternal Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroupexternal_id** | **int** | The unique ID of the Usergroupexternal | 
**s_usergroupexternal_name** | **str** | The name of the Usergroupexternal | 
**s_usergroupexternal_id** | **str** | The id of the Usergroupexternal | 

## Example

```python
from eZmaxApi.models.usergroupexternal_response_compound import UsergroupexternalResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalResponseCompound from a JSON string
usergroupexternal_response_compound_instance = UsergroupexternalResponseCompound.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalResponseCompound.to_json())

# convert the object into a dict
usergroupexternal_response_compound_dict = usergroupexternal_response_compound_instance.to_dict()
# create an instance of UsergroupexternalResponseCompound from a dict
usergroupexternal_response_compound_from_dict = UsergroupexternalResponseCompound.from_dict(usergroupexternal_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


