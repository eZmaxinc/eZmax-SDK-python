# EzsignelementdependencyRequestCompound

An Ezsignelementdependency Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignelementdependency_id** | **int** | The unique ID of the Ezsignelementdependency | [optional] 
**fki_ezsignformfield_id_validation** | **int** | The unique ID of the Ezsignformfield | [optional] 
**fki_ezsignformfieldgroup_id_validation** | **int** | The unique ID of the Ezsignformfieldgroup | [optional] 
**s_ezsignelementdependency_ezsignformfieldgrouplabel** | **str** | The Label for the Ezsignformfieldgroup | [optional] 
**s_ezsignelementdependency_ezsignformfieldlabel** | **str** | The Label for the Ezsignformfield | [optional] 
**e_ezsignelementdependency_validation** | [**FieldEEzsignelementdependencyValidation**](FieldEEzsignelementdependencyValidation.md) |  | 
**b_ezsignelementdependency_selected** | **bool** | Whether if it&#39;s selected or not when using eEzsignelementdependencyValidation &#x3D; Selected | [optional] 
**e_ezsignelementdependency_operator** | [**FieldEEzsignelementdependencyOperator**](FieldEEzsignelementdependencyOperator.md) |  | [optional] 
**s_ezsignelementdependency_value** | **str** | The value of the Ezsignelementdependency | [optional] 

## Example

```python
from eZmaxApi.models.ezsignelementdependency_request_compound import EzsignelementdependencyRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignelementdependencyRequestCompound from a JSON string
ezsignelementdependency_request_compound_instance = EzsignelementdependencyRequestCompound.from_json(json)
# print the JSON string representation of the object
print EzsignelementdependencyRequestCompound.to_json()

# convert the object into a dict
ezsignelementdependency_request_compound_dict = ezsignelementdependency_request_compound_instance.to_dict()
# create an instance of EzsignelementdependencyRequestCompound from a dict
ezsignelementdependency_request_compound_form_dict = ezsignelementdependency_request_compound.from_dict(ezsignelementdependency_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


