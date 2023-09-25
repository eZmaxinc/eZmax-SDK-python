# MultilingualVariableexpenseDescription

The description of the Variableexpense

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_variableexpense_description1** | **str** | The description of the Variableexpense in French | [optional] 
**s_variableexpense_description2** | **str** | The description of the Variableexpense in English | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_variableexpense_description import MultilingualVariableexpenseDescription

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualVariableexpenseDescription from a JSON string
multilingual_variableexpense_description_instance = MultilingualVariableexpenseDescription.from_json(json)
# print the JSON string representation of the object
print MultilingualVariableexpenseDescription.to_json()

# convert the object into a dict
multilingual_variableexpense_description_dict = multilingual_variableexpense_description_instance.to_dict()
# create an instance of MultilingualVariableexpenseDescription from a dict
multilingual_variableexpense_description_form_dict = multilingual_variableexpense_description.from_dict(multilingual_variableexpense_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


