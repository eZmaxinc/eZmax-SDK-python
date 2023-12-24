# VariableexpenseRequestCompound

A Variableexpense Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_variableexpense_id** | **int** | The unique ID of the Variableexpense | [optional] 
**s_variableexpense_code** | **str** | The code of the Variableexpense | 
**obj_variableexpense_description** | [**MultilingualVariableexpenseDescription**](MultilingualVariableexpenseDescription.md) |  | 
**e_variableexpense_taxable** | [**FieldEVariableexpenseTaxable**](FieldEVariableexpenseTaxable.md) |  | 
**b_variableexpense_isactive** | **bool** | Whether the variableexpense is active or not | 

## Example

```python
from eZmaxApi.models.variableexpense_request_compound import VariableexpenseRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of VariableexpenseRequestCompound from a JSON string
variableexpense_request_compound_instance = VariableexpenseRequestCompound.from_json(json)
# print the JSON string representation of the object
print VariableexpenseRequestCompound.to_json()

# convert the object into a dict
variableexpense_request_compound_dict = variableexpense_request_compound_instance.to_dict()
# create an instance of VariableexpenseRequestCompound from a dict
variableexpense_request_compound_form_dict = variableexpense_request_compound.from_dict(variableexpense_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


