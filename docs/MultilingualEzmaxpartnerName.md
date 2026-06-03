# MultilingualEzmaxpartnerName

Name of the Ezmaxpartner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_ezmaxpartner_name1** | **str** | The name of the Ezmaxpartner in french | [optional] 
**s_ezmaxpartner_name2** | **str** | The name of the Ezmaxpartner in english | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_ezmaxpartner_name import MultilingualEzmaxpartnerName

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualEzmaxpartnerName from a JSON string
multilingual_ezmaxpartner_name_instance = MultilingualEzmaxpartnerName.from_json(json)
# print the JSON string representation of the object
print(MultilingualEzmaxpartnerName.to_json())

# convert the object into a dict
multilingual_ezmaxpartner_name_dict = multilingual_ezmaxpartner_name_instance.to_dict()
# create an instance of MultilingualEzmaxpartnerName from a dict
multilingual_ezmaxpartner_name_from_dict = MultilingualEzmaxpartnerName.from_dict(multilingual_ezmaxpartner_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


