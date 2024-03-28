# EzsignannotationResponseCompound

A Ezsignannotation Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignannotation_id** | **int** | The unique ID of the Ezsignannotation | 
**fki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | 
**e_ezsignannotation_horizontalalignment** | [**EnumHorizontalalignment**](EnumHorizontalalignment.md) |  | [optional] 
**e_ezsignannotation_verticalalignment** | [**EnumVerticalalignment**](EnumVerticalalignment.md) |  | [optional] 
**e_ezsignannotation_type** | [**FieldEEzsignannotationType**](FieldEEzsignannotationType.md) |  | 
**i_ezsignannotation_x** | **int** | The X coordinate (Horizontal) where to put the Ezsignannotation on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignannotation 2 inches from the left border of the page, you would use \&quot;200\&quot; for the X coordinate. | 
**i_ezsignannotation_y** | **int** | The Y coordinate (Vertical) where to put the Ezsignannotation on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignannotation 3 inches from the top border of the page, you would use \&quot;300\&quot; for the Y coordinate. | 
**i_ezsignannotation_width** | **int** | The Width of the Ezsignannotation.  Width is calculated at 100dpi (dot per inch). So for example, if you want to have the width of the Ezsignannotation to be 3 inches, you would use \&quot;300\&quot; for the Width. | [optional] 
**i_ezsignannotation_height** | **int** | The Height of the Ezsignannotation.  Height is calculated at 100dpi (dot per inch). So for example, if you want to have the height of the Ezsignannotation to be 2 inches, you would use \&quot;200\&quot; for the Height.  This can only be set if eEzsignannotationType is **StrikethroughBlock** or **Text** | [optional] 
**s_ezsignannotation_text** | **str** | The Text of the Ezsignannotation | [optional] 
**i_ezsignpage_pagenumber** | **int** | The page number in the Ezsigndocument | 
**obj_textstylestatic** | [**TextstylestaticResponseCompound**](TextstylestaticResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignannotation_response_compound import EzsignannotationResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignannotationResponseCompound from a JSON string
ezsignannotation_response_compound_instance = EzsignannotationResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignannotationResponseCompound.to_json())

# convert the object into a dict
ezsignannotation_response_compound_dict = ezsignannotation_response_compound_instance.to_dict()
# create an instance of EzsignannotationResponseCompound from a dict
ezsignannotation_response_compound_form_dict = ezsignannotation_response_compound.from_dict(ezsignannotation_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


