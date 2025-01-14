# MultilingualBrandingDescription

Description of the Branding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_branding_description1** | **str** | The description of the Branding in French | [optional] 
**s_branding_description2** | **str** | The description of the Branding in English | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_branding_description import MultilingualBrandingDescription

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualBrandingDescription from a JSON string
multilingual_branding_description_instance = MultilingualBrandingDescription.from_json(json)
# print the JSON string representation of the object
print(MultilingualBrandingDescription.to_json())

# convert the object into a dict
multilingual_branding_description_dict = multilingual_branding_description_instance.to_dict()
# create an instance of MultilingualBrandingDescription from a dict
multilingual_branding_description_from_dict = MultilingualBrandingDescription.from_dict(multilingual_branding_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


