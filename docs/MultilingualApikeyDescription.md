# MultilingualApikeyDescription

Description of the API Key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_apikey_description1** | **str** | The description of the Apikey in French | [optional] 
**s_apikey_description2** | **str** | The description of the Apikey in English | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_apikey_description import MultilingualApikeyDescription

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualApikeyDescription from a JSON string
multilingual_apikey_description_instance = MultilingualApikeyDescription.from_json(json)
# print the JSON string representation of the object
print MultilingualApikeyDescription.to_json()

# convert the object into a dict
multilingual_apikey_description_dict = multilingual_apikey_description_instance.to_dict()
# create an instance of MultilingualApikeyDescription from a dict
multilingual_apikey_description_form_dict = multilingual_apikey_description.from_dict(multilingual_apikey_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


