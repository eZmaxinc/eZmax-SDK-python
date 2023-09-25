# VariableexpenseResponse

A Variableexpense Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_variableexpense_id** | **int** | The unique ID of the Variableexpense | 
**s_variableexpense_code** | **str** | The code of the Variableexpense | [optional] 
**obj_variableexpense_description** | [**MultilingualVariableexpenseDescription**](MultilingualVariableexpenseDescription.md) |  | 
**e_variableexpense_taxable** | [**FieldEVariableexpenseTaxable**](FieldEVariableexpenseTaxable.md) |  | [optional] 
**b_variableexpense_isactive** | **bool** | Whether the variableexpense is active or not | [optional] 

## Example

```python
from eZmaxApi.models.variableexpense_response import VariableexpenseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VariableexpenseResponse from a JSON string
variableexpense_response_instance = VariableexpenseResponse.from_json(json)
# print the JSON string representation of the object
print VariableexpenseResponse.to_json()

# convert the object into a dict
variableexpense_response_dict = variableexpense_response_instance.to_dict()
# create an instance of VariableexpenseResponse from a dict
variableexpense_response_form_dict = variableexpense_response.from_dict(variableexpense_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


