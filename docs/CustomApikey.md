# CustomApikey

A Custom Apikey Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_apikey_key** | **str** | The key of the Apikey | 
**s_apikey_secret** | **str** | The secret of the Apikey | 

## Example

```python
from eZmaxApi.models.custom_apikey import CustomApikey

# TODO update the JSON string below
json = "{}"
# create an instance of CustomApikey from a JSON string
custom_apikey_instance = CustomApikey.from_json(json)
# print the JSON string representation of the object
print(CustomApikey.to_json())

# convert the object into a dict
custom_apikey_dict = custom_apikey_instance.to_dict()
# create an instance of CustomApikey from a dict
custom_apikey_from_dict = CustomApikey.from_dict(custom_apikey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


