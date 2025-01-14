# EzsigntemplateelementdependencyResponse

An Ezsigntemplateelementdependency Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateelementdependency_id** | **int** | The unique ID of the Ezsigntemplateelementdependency | 
**fki_ezsigntemplateformfield_id** | **int** | The unique ID of the Ezsigntemplateformfield | [optional] 
**fki_ezsigntemplatesignature_id** | **int** | The unique ID of the Ezsigntemplatesignature | [optional] 
**fki_ezsigntemplateformfield_id_validation** | **int** | The unique ID of the Ezsigntemplateformfield | [optional] 
**fki_ezsigntemplateformfieldgroup_id_validation** | **int** | The unique ID of the Ezsigntemplateformfieldgroup | [optional] 
**e_ezsigntemplateelementdependency_validation** | [**FieldEEzsigntemplateelementdependencyValidation**](FieldEEzsigntemplateelementdependencyValidation.md) |  | 
**b_ezsigntemplateelementdependency_selected** | **bool** | Whether if it&#39;s selected or not when using eEzsigntemplateelementdependencyValidation &#x3D; Selected | [optional] 
**e_ezsigntemplateelementdependency_operator** | [**FieldEEzsigntemplateelementdependencyOperator**](FieldEEzsigntemplateelementdependencyOperator.md) |  | [optional] 
**s_ezsigntemplateelementdependency_value** | **str** | The value of the Ezsignelementdependency | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplateelementdependency_response import EzsigntemplateelementdependencyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateelementdependencyResponse from a JSON string
ezsigntemplateelementdependency_response_instance = EzsigntemplateelementdependencyResponse.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateelementdependencyResponse.to_json())

# convert the object into a dict
ezsigntemplateelementdependency_response_dict = ezsigntemplateelementdependency_response_instance.to_dict()
# create an instance of EzsigntemplateelementdependencyResponse from a dict
ezsigntemplateelementdependency_response_from_dict = EzsigntemplateelementdependencyResponse.from_dict(ezsigntemplateelementdependency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


