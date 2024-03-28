# UsergroupexternalRequestCompound

A Usergroupexternal Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroupexternal_id** | **int** | The unique ID of the Usergroupexternal | [optional] 
**s_usergroupexternal_name** | **str** | The name of the Usergroupexternal | 
**s_usergroupexternal_id** | **str** | The id of the Usergroupexternal | 

## Example

```python
from eZmaxApi.models.usergroupexternal_request_compound import UsergroupexternalRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalRequestCompound from a JSON string
usergroupexternal_request_compound_instance = UsergroupexternalRequestCompound.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalRequestCompound.to_json())

# convert the object into a dict
usergroupexternal_request_compound_dict = usergroupexternal_request_compound_instance.to_dict()
# create an instance of UsergroupexternalRequestCompound from a dict
usergroupexternal_request_compound_form_dict = usergroupexternal_request_compound.from_dict(usergroupexternal_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


