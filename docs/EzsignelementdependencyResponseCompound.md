# EzsignelementdependencyResponseCompound

An Ezsignelementdependency Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignelementdependency_id** | **int** | The unique ID of the Ezsignelementdependency | 
**fki_ezsignformfield_id** | **int** | The unique ID of the Ezsignformfield | [optional] 
**fki_ezsignsignature_id** | **int** | The unique ID of the Ezsignsignature | [optional] 
**fki_ezsignformfield_id_validation** | **int** | The unique ID of the Ezsignformfield | [optional] 
**fki_ezsignformfieldgroup_id_validation** | **int** | The unique ID of the Ezsignformfieldgroup | [optional] 
**e_ezsignelementdependency_validation** | [**FieldEEzsignelementdependencyValidation**](FieldEEzsignelementdependencyValidation.md) |  | 
**b_ezsignelementdependency_selected** | **bool** | Whether if it&#39;s selected or not when using eEzsignelementdependencyValidation &#x3D; Selected | [optional] 
**e_ezsignelementdependency_operator** | [**FieldEEzsignelementdependencyOperator**](FieldEEzsignelementdependencyOperator.md) |  | [optional] 
**s_ezsignelementdependency_value** | **str** | The value of the Ezsignelementdependency | [optional] 

## Example

```python
from eZmaxApi.models.ezsignelementdependency_response_compound import EzsignelementdependencyResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignelementdependencyResponseCompound from a JSON string
ezsignelementdependency_response_compound_instance = EzsignelementdependencyResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignelementdependencyResponseCompound.to_json())

# convert the object into a dict
ezsignelementdependency_response_compound_dict = ezsignelementdependency_response_compound_instance.to_dict()
# create an instance of EzsignelementdependencyResponseCompound from a dict
ezsignelementdependency_response_compound_from_dict = EzsignelementdependencyResponseCompound.from_dict(ezsignelementdependency_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


