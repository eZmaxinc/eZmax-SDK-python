# EzsigntemplateelementdependencyRequestCompound

An Ezsigntemplateelementdependency Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateelementdependency_id** | **int** | The unique ID of the Ezsigntemplateelementdependency | [optional] 
**fki_ezsigntemplateformfield_id_validation** | **int** | The unique ID of the Ezsigntemplateformfield | [optional] 
**fki_ezsigntemplateformfieldgroup_id_validation** | **int** | The unique ID of the Ezsigntemplateformfieldgroup | [optional] 
**s_ezsigntemplateelementdependency_ezsigntemplateformfieldgrouplabel** | **str** | The Label for the Ezsigntemplateformfieldgroup | [optional] 
**s_ezsigntemplateelementdependency_ezsigntemplateformfieldlabel** | **str** | The Label for the Ezsigntemplateformfield | [optional] 
**e_ezsigntemplateelementdependency_validation** | [**FieldEEzsigntemplateelementdependencyValidation**](FieldEEzsigntemplateelementdependencyValidation.md) |  | 
**b_ezsigntemplateelementdependency_selected** | **bool** | Whether if it&#39;s selected or not when using eEzsigntemplateelementdependencyValidation &#x3D; Selected | [optional] 
**e_ezsigntemplateelementdependency_operator** | [**FieldEEzsigntemplateelementdependencyOperator**](FieldEEzsigntemplateelementdependencyOperator.md) |  | [optional] 
**s_ezsigntemplateelementdependency_value** | **str** | The value of the Ezsignelementdependency | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplateelementdependency_request_compound import EzsigntemplateelementdependencyRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateelementdependencyRequestCompound from a JSON string
ezsigntemplateelementdependency_request_compound_instance = EzsigntemplateelementdependencyRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateelementdependencyRequestCompound.to_json())

# convert the object into a dict
ezsigntemplateelementdependency_request_compound_dict = ezsigntemplateelementdependency_request_compound_instance.to_dict()
# create an instance of EzsigntemplateelementdependencyRequestCompound from a dict
ezsigntemplateelementdependency_request_compound_from_dict = EzsigntemplateelementdependencyRequestCompound.from_dict(ezsigntemplateelementdependency_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


