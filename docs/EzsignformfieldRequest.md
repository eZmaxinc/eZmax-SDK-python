# EzsignformfieldRequest

A Ezsignformfield Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignformfield_id** | **int** | The unique ID of the Ezsignformfield | [optional] 
**i_ezsignpage_pagenumber** | **int** | The page number in the Ezsigndocument | 
**s_ezsignformfield_label** | **str** | The Label for the Ezsignformfield | 
**s_ezsignformfield_value** | **str** | The value for the Ezsignformfield  This can only be set if eEzsignformfieldgroupType is Checkbox or Radio | [optional] 
**i_ezsignformfield_x** | **int** | The X coordinate (Horizontal) where to put the Ezsignformfield on the Ezsignpage.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignformfield 2 inches from the left border of the page, you would use \&quot;200\&quot; for the X coordinate. | 
**i_ezsignformfield_y** | **int** | The Y coordinate (Vertical) where to put the Ezsignformfield on the Ezsignpage.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignformfield 3 inches from the top border of the page, you would use \&quot;300\&quot; for the Y coordinate. | 
**i_ezsignformfield_width** | **int** | The Width of the Ezsignformfield in pixels calculated at 100 DPI | 
**i_ezsignformfield_height** | **int** | The Height of the Ezsignformfield in pixels calculated at 100 DPI  | 
**b_ezsignformfield_autocomplete** | **bool** | Whether the Ezsignformfield allows the use of the autocomplete of the browser.  This can only be set if eEzsignformfieldgroupType is **Text** | [optional] 
**b_ezsignformfield_selected** | **bool** | Whether the Ezsignformfield is selected or not by default.  This can only be set if eEzsignformfieldgroupType is **Checkbox** or **Radio** | [optional] 
**s_ezsignformfield_enteredvalue** | **str** | This is the value enterred for the Ezsignformfield  This can only be set if eEzsignformfieldgroupType is **Dropdown**, **Text** or **Textarea** | [optional] 
**e_ezsignformfield_dependencyrequirement** | [**FieldEEzsignformfieldDependencyrequirement**](FieldEEzsignformfieldDependencyrequirement.md) |  | [optional] 
**e_ezsignformfield_horizontalalignment** | [**EnumHorizontalalignment**](EnumHorizontalalignment.md) |  | [optional] 
**obj_textstylestatic** | [**TextstylestaticRequestCompound**](TextstylestaticRequestCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignformfield_request import EzsignformfieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignformfieldRequest from a JSON string
ezsignformfield_request_instance = EzsignformfieldRequest.from_json(json)
# print the JSON string representation of the object
print(EzsignformfieldRequest.to_json())

# convert the object into a dict
ezsignformfield_request_dict = ezsignformfield_request_instance.to_dict()
# create an instance of EzsignformfieldRequest from a dict
ezsignformfield_request_from_dict = EzsignformfieldRequest.from_dict(ezsignformfield_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


