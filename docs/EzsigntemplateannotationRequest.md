# EzsigntemplateannotationRequest

A Ezsigntemplateannotation Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateannotation_id** | **int** | The unique ID of the Ezsigntemplateannotation | [optional] 
**fki_ezsigntemplatedocument_id** | **int** | The unique ID of the Ezsigntemplatedocument | 
**e_ezsigntemplateannotation_horizontalalignment** | [**FieldEEzsigntemplateannotationHorizontalalignment**](FieldEEzsigntemplateannotationHorizontalalignment.md) |  | 
**e_ezsigntemplateannotation_verticalalignment** | [**FieldEEzsigntemplateannotationVerticalalignment**](FieldEEzsigntemplateannotationVerticalalignment.md) |  | 
**e_ezsigntemplateannotation_type** | [**FieldEEzsigntemplateannotationType**](FieldEEzsigntemplateannotationType.md) |  | 
**i_ezsigntemplateannotation_x** | **int** | The x of the Ezsigntemplateannotation | 
**i_ezsigntemplateannotation_y** | **int** | The y of the Ezsigntemplateannotation | 
**i_ezsigntemplateannotation_width** | **int** | The width of the Ezsigntemplateannotation | 
**i_ezsigntemplateannotation_height** | **int** | The height of the Ezsigntemplateannotation | 
**i_ezsigntemplatedocumentpage_pagenumber** | **int** | The page number in the Ezsigntemplatedocument | 
**s_ezsigntemplateannotation_description** | **str** | The description of the Ezsigntemplateannotation | 
**s_ezsigntemplateannotation_defaulttext** | **str** | The defaulttext of the Ezsigntemplateannotation | 
**s_ezsigntemplateannotation_dropdownvalues** | **str** | The ndropdownvalues of the Ezsigntemplateannotation | 
**obj_textstylestatic** | [**TextstylestaticRequestCompound**](TextstylestaticRequestCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplateannotation_request import EzsigntemplateannotationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateannotationRequest from a JSON string
ezsigntemplateannotation_request_instance = EzsigntemplateannotationRequest.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateannotationRequest.to_json())

# convert the object into a dict
ezsigntemplateannotation_request_dict = ezsigntemplateannotation_request_instance.to_dict()
# create an instance of EzsigntemplateannotationRequest from a dict
ezsigntemplateannotation_request_from_dict = EzsigntemplateannotationRequest.from_dict(ezsigntemplateannotation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


