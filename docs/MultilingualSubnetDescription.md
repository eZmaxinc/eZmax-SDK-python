# MultilingualSubnetDescription

The description of the Subnet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_subnet_description1** | **str** | The description of the Subnet in French | [optional] 
**s_subnet_description2** | **str** | The description of the Subnet in English | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_subnet_description import MultilingualSubnetDescription

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualSubnetDescription from a JSON string
multilingual_subnet_description_instance = MultilingualSubnetDescription.from_json(json)
# print the JSON string representation of the object
print(MultilingualSubnetDescription.to_json())

# convert the object into a dict
multilingual_subnet_description_dict = multilingual_subnet_description_instance.to_dict()
# create an instance of MultilingualSubnetDescription from a dict
multilingual_subnet_description_from_dict = MultilingualSubnetDescription.from_dict(multilingual_subnet_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


