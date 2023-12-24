# VariableexpenseRequest

A Variableexpense Object

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
from eZmaxApi.models.variableexpense_request import VariableexpenseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VariableexpenseRequest from a JSON string
variableexpense_request_instance = VariableexpenseRequest.from_json(json)
# print the JSON string representation of the object
print VariableexpenseRequest.to_json()

# convert the object into a dict
variableexpense_request_dict = variableexpense_request_instance.to_dict()
# create an instance of VariableexpenseRequest from a dict
variableexpense_request_form_dict = variableexpense_request.from_dict(variableexpense_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


