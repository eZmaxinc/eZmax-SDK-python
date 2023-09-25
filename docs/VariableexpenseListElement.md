# VariableexpenseListElement

A Variableexpense List Element

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_variableexpense_id** | **int** | The unique ID of the Variableexpense | 
**s_variableexpense_code** | **str** | The code of the Variableexpense | [optional] 
**s_variableexpense_description_x** | **str** | The description of the Variableexpense in the language of the requester | [optional] 
**e_variableexpense_taxable** | [**FieldEVariableexpenseTaxable**](FieldEVariableexpenseTaxable.md) |  | [optional] 
**b_variableexpense_isactive** | **bool** | Whether the variableexpense is active or not | [optional] 

## Example

```python
from eZmaxApi.models.variableexpense_list_element import VariableexpenseListElement

# TODO update the JSON string below
json = "{}"
# create an instance of VariableexpenseListElement from a JSON string
variableexpense_list_element_instance = VariableexpenseListElement.from_json(json)
# print the JSON string representation of the object
print VariableexpenseListElement.to_json()

# convert the object into a dict
variableexpense_list_element_dict = variableexpense_list_element_instance.to_dict()
# create an instance of VariableexpenseListElement from a dict
variableexpense_list_element_form_dict = variableexpense_list_element.from_dict(variableexpense_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


