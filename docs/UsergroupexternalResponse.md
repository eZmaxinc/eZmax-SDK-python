# UsergroupexternalResponse

A Usergroupexternal Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroupexternal_id** | **int** | The unique ID of the Usergroupexternal | 
**s_usergroupexternal_name** | **str** | The name of the Usergroupexternal | 
**s_usergroupexternal_id** | **str** | The id of the Usergroupexternal | 

## Example

```python
from eZmaxApi.models.usergroupexternal_response import UsergroupexternalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalResponse from a JSON string
usergroupexternal_response_instance = UsergroupexternalResponse.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalResponse.to_json())

# convert the object into a dict
usergroupexternal_response_dict = usergroupexternal_response_instance.to_dict()
# create an instance of UsergroupexternalResponse from a dict
usergroupexternal_response_form_dict = usergroupexternal_response.from_dict(usergroupexternal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


