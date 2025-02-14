# EzsigntemplateformfieldRequest

A Ezsigntemplateformfield Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateformfield_id** | **int** | The unique ID of the Ezsigntemplateformfield | [optional] 
**e_ezsigntemplateformfield_positioning** | [**FieldEEzsigntemplateformfieldPositioning**](FieldEEzsigntemplateformfieldPositioning.md) |  | [optional] [default to FieldEEzsigntemplateformfieldPositioning.PERCOORDINATES]
**i_ezsigntemplatedocumentpage_pagenumber** | **int** | The page number in the Ezsigntemplatedocument | 
**s_ezsigntemplateformfield_label** | **str** | The Label for the Ezsigntemplateformfield | 
**s_ezsigntemplateformfield_value** | **str** | The value for the Ezsigntemplateformfield | [optional] 
**i_ezsigntemplateformfield_x** | **int** | The X coordinate (Horizontal) where to put the Ezsigntemplateformfield on the Ezsigntemplatepage.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsigntemplateformfield 2 inches from the left border of the page, you would use \&quot;200\&quot; for the X coordinate. | [optional] 
**i_ezsigntemplateformfield_y** | **int** | The Y coordinate (Vertical) where to put the Ezsigntemplateformfield on the Ezsigntemplatepage.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsigntemplateformfield 3 inches from the top border of the page, you would use \&quot;300\&quot; for the Y coordinate. | [optional] 
**i_ezsigntemplateformfield_width** | **int** | The Width of the Ezsigntemplateformfield in pixels calculated at 100 DPI | 
**i_ezsigntemplateformfield_height** | **int** | The Height of the Ezsigntemplateformfield in pixels calculated at 100 DPI  | 
**b_ezsigntemplateformfield_autocomplete** | **bool** | Whether the Ezsigntemplateformfield allows the use of the autocomplete of the browser.  This can only be set if eEzsigntemplateformfieldgroupType is **Text** | [optional] 
**b_ezsigntemplateformfield_selected** | **bool** | Whether the Ezsigntemplateformfield is selected or not by default.  This can only be set if eEzsigntemplateformfieldgroupType is **Checkbox** or **Radio** | [optional] 
**e_ezsigntemplateformfield_dependencyrequirement** | [**FieldEEzsigntemplateformfieldDependencyrequirement**](FieldEEzsigntemplateformfieldDependencyrequirement.md) |  | [optional] 
**s_ezsigntemplateformfield_positioningpattern** | **str** | The string pattern to search for the positioning. **This is not a regexp**  This will be required if **eEzsigntemplateformfieldPositioning** is set to **PerCoordinates** | [optional] 
**i_ezsigntemplateformfield_positioningoffsetx** | **int** | The offset X  This will be required if **eEzsigntemplateformfieldPositioning** is set to **PerCoordinates** | [optional] 
**i_ezsigntemplateformfield_positioningoffsety** | **int** | The offset Y  This will be required if **eEzsigntemplateformfieldPositioning** is set to **PerCoordinates** | [optional] 
**e_ezsigntemplateformfield_positioningoccurence** | [**FieldEEzsigntemplateformfieldPositioningoccurence**](FieldEEzsigntemplateformfieldPositioningoccurence.md) |  | [optional] 
**e_ezsigntemplateformfield_horizontalalignment** | [**EnumHorizontalalignment**](EnumHorizontalalignment.md) |  | [optional] 
**obj_textstylestatic** | [**TextstylestaticRequestCompound**](TextstylestaticRequestCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplateformfield_request import EzsigntemplateformfieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateformfieldRequest from a JSON string
ezsigntemplateformfield_request_instance = EzsigntemplateformfieldRequest.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateformfieldRequest.to_json())

# convert the object into a dict
ezsigntemplateformfield_request_dict = ezsigntemplateformfield_request_instance.to_dict()
# create an instance of EzsigntemplateformfieldRequest from a dict
ezsigntemplateformfield_request_from_dict = EzsigntemplateformfieldRequest.from_dict(ezsigntemplateformfield_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


