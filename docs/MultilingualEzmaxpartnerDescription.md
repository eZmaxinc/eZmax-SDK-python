# MultilingualEzmaxpartnerDescription

Description of the Ezmaxpartner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_ezmaxpartner_description1** | **str** | The description of the Ezmaxpartner in french | [optional] 
**s_ezmaxpartner_description2** | **str** | The description of the Ezmaxpartner in english | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_ezmaxpartner_description import MultilingualEzmaxpartnerDescription

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualEzmaxpartnerDescription from a JSON string
multilingual_ezmaxpartner_description_instance = MultilingualEzmaxpartnerDescription.from_json(json)
# print the JSON string representation of the object
print(MultilingualEzmaxpartnerDescription.to_json())

# convert the object into a dict
multilingual_ezmaxpartner_description_dict = multilingual_ezmaxpartner_description_instance.to_dict()
# create an instance of MultilingualEzmaxpartnerDescription from a dict
multilingual_ezmaxpartner_description_from_dict = MultilingualEzmaxpartnerDescription.from_dict(multilingual_ezmaxpartner_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


