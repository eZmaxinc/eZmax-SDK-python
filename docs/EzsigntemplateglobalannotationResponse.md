# EzsigntemplateglobalannotationResponse

A Ezsigntemplateglobalannotation Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateglobalannotation_id** | **int** | The unique ID of the Ezsigntemplateglobalannotation | 
**fki_textstylestatic_id** | **int** | The unique ID of the Textstylestatic | [optional] 
**obj_textstylestatic** | [**TextstylestaticRequestCompound**](TextstylestaticRequestCompound.md) |  | [optional] 
**e_ezsigntemplateglobalannotation_horizontalalignment** | [**FieldEEzsigntemplateglobalannotationHorizontalalignment**](FieldEEzsigntemplateglobalannotationHorizontalalignment.md) |  | 
**e_ezsigntemplateglobalannotation_verticalalignment** | [**FieldEEzsigntemplateglobalannotationVerticalalignment**](FieldEEzsigntemplateglobalannotationVerticalalignment.md) |  | 
**e_ezsigntemplateglobalannotation_type** | [**FieldEEzsigntemplateglobalannotationType**](FieldEEzsigntemplateglobalannotationType.md) |  | 
**i_ezsigntemplateglobalannotation_x** | **int** | The x of the Ezsigntemplateglobalannotation | 
**i_ezsigntemplateglobalannotation_y** | **int** | The y of the Ezsigntemplateglobalannotation | 
**i_ezsigntemplateglobalannotation_width** | **int** | The width of the Ezsigntemplateglobalannotation | 
**i_ezsigntemplateglobalannotation_height** | **int** | The height of the Ezsigntemplateglobalannotation | 
**i_ezsigntemplateglobaldocumentpage_pagenumber** | **int** | The page number in the Ezsigntemplateglobaldocument | 
**s_ezsigntemplateglobalannotation_description** | **str** | The description of the Ezsigntemplateglobalannotation | 
**s_ezsigntemplateglobalannotation_defaulttext** | **str** | The defaulttext of the Ezsigntemplateglobalannotation | 
**s_ezsigntemplateglobalannotation_dropdownvalues** | **str** | The dropdownvalues of the Ezsigntemplateglobalannotation | 

## Example

```python
from eZmaxApi.models.ezsigntemplateglobalannotation_response import EzsigntemplateglobalannotationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateglobalannotationResponse from a JSON string
ezsigntemplateglobalannotation_response_instance = EzsigntemplateglobalannotationResponse.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateglobalannotationResponse.to_json())

# convert the object into a dict
ezsigntemplateglobalannotation_response_dict = ezsigntemplateglobalannotation_response_instance.to_dict()
# create an instance of EzsigntemplateglobalannotationResponse from a dict
ezsigntemplateglobalannotation_response_from_dict = EzsigntemplateglobalannotationResponse.from_dict(ezsigntemplateglobalannotation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


