# EzsigntemplateformfieldRequest

A Ezsigntemplateformfield Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateformfield_id** | **int** | The unique ID of the Ezsigntemplateformfield | [optional] 
**i_ezsigntemplatedocumentpage_pagenumber** | **int** | The page number in the Ezsigntemplatedocument | 
**s_ezsigntemplateformfield_label** | **str** | The Label for the Ezsigntemplateformfield | 
**s_ezsigntemplateformfield_value** | **str** | The value for the Ezsigntemplateformfield | [optional] 
**i_ezsigntemplateformfield_x** | **int** | The X coordinate (Horizontal) where to put the Ezsigntemplateformfield on the Ezsigntemplatepage.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsigntemplateformfield 2 inches from the left border of the page, you would use \&quot;200\&quot; for the X coordinate. | 
**i_ezsigntemplateformfield_y** | **int** | The Y coordinate (Vertical) where to put the Ezsigntemplateformfield on the Ezsigntemplatepage.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsigntemplateformfield 3 inches from the top border of the page, you would use \&quot;300\&quot; for the Y coordinate. | 
**i_ezsigntemplateformfield_width** | **int** | The Width of the Ezsigntemplateformfield in pixels calculated at 100 DPI  The allowed values are varying based on the eEzsigntemplateformfieldgroupType.  | eEzsigntemplateformfieldgroupType | Valid values | | ------------------------- | ------------ | | Checkbox                  | 22           | | Dropdown                  | 22-65535     | | Radio                     | 22           | | Text                      | 22-65535     | | Textarea                  | 22-65535     | | 
**i_ezsigntemplateformfield_height** | **int** | The Height of the Ezsigntemplateformfield in pixels calculated at 100 DPI  The allowed values are varying based on the eEzsigntemplateformfieldgroupType.  | eEzsigntemplateformfieldgroupType | Valid values | | ------------------------- | ------------ | | Checkbox                  | 22           | | Dropdown                  | 22           | | Radio                     | 22           | | Text                      | 22           | | Textarea                  | 22-65535     |  | 
**b_ezsigntemplateformfield_autocomplete** | **bool** | Whether the Ezsigntemplateformfield allows the use of the autocomplete of the browser.  This can only be set if eEzsigntemplateformfieldgroupType is **Text** | [optional] 
**b_ezsigntemplateformfield_selected** | **bool** | Whether the Ezsigntemplateformfield is selected or not by default.  This can only be set if eEzsigntemplateformfieldgroupType is **Checkbox** or **Radio** | [optional] 
**e_ezsigntemplateformfield_dependencyrequirement** | [**FieldEEzsigntemplateformfieldDependencyrequirement**](FieldEEzsigntemplateformfieldDependencyrequirement.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplateformfield_request import EzsigntemplateformfieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateformfieldRequest from a JSON string
ezsigntemplateformfield_request_instance = EzsigntemplateformfieldRequest.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateformfieldRequest.to_json()

# convert the object into a dict
ezsigntemplateformfield_request_dict = ezsigntemplateformfield_request_instance.to_dict()
# create an instance of EzsigntemplateformfieldRequest from a dict
ezsigntemplateformfield_request_form_dict = ezsigntemplateformfield_request.from_dict(ezsigntemplateformfield_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


