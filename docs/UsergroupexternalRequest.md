# UsergroupexternalRequest

A Usergroupexternal Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroupexternal_id** | **int** | The unique ID of the Usergroupexternal | [optional] 
**s_usergroupexternal_name** | **str** | The name of the Usergroupexternal | 
**s_usergroupexternal_id** | **str** | The id of the Usergroupexternal | 

## Example

```python
from eZmaxApi.models.usergroupexternal_request import UsergroupexternalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalRequest from a JSON string
usergroupexternal_request_instance = UsergroupexternalRequest.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalRequest.to_json())

# convert the object into a dict
usergroupexternal_request_dict = usergroupexternal_request_instance.to_dict()
# create an instance of UsergroupexternalRequest from a dict
usergroupexternal_request_from_dict = UsergroupexternalRequest.from_dict(usergroupexternal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


