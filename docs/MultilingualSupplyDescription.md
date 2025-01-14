# MultilingualSupplyDescription

The description1 of the Supply

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_supply_description1** | **str** | The description of the Supply in French | [optional] 
**s_supply_description2** | **str** | The description of the Supply in English | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_supply_description import MultilingualSupplyDescription

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualSupplyDescription from a JSON string
multilingual_supply_description_instance = MultilingualSupplyDescription.from_json(json)
# print the JSON string representation of the object
print(MultilingualSupplyDescription.to_json())

# convert the object into a dict
multilingual_supply_description_dict = multilingual_supply_description_instance.to_dict()
# create an instance of MultilingualSupplyDescription from a dict
multilingual_supply_description_from_dict = MultilingualSupplyDescription.from_dict(multilingual_supply_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


