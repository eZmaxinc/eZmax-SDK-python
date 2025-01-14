# CustomApikeyfederation

A Custom Apikeyfederation Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_apikeyfederation_key** | **str** | The key of the Apikeyfederation | 
**s_apikeyfederation_secret** | **str** | The secret of the Apikeyfederation | 

## Example

```python
from eZmaxApi.models.custom_apikeyfederation import CustomApikeyfederation

# TODO update the JSON string below
json = "{}"
# create an instance of CustomApikeyfederation from a JSON string
custom_apikeyfederation_instance = CustomApikeyfederation.from_json(json)
# print the JSON string representation of the object
print(CustomApikeyfederation.to_json())

# convert the object into a dict
custom_apikeyfederation_dict = custom_apikeyfederation_instance.to_dict()
# create an instance of CustomApikeyfederation from a dict
custom_apikeyfederation_from_dict = CustomApikeyfederation.from_dict(custom_apikeyfederation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


