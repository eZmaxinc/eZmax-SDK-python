# EzsigntemplatesignatureResponse

A Ezsigntemplatesignature Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatesignature_id** | **int** | The unique ID of the Ezsigntemplatesignature | 
**fki_ezsigntemplatedocument_id** | **int** | The unique ID of the Ezsigntemplatedocument | 
**fki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | 
**fki_ezsigntemplatesigner_id_validation** | **int** | The unique ID of the Ezsigntemplatesigner | [optional] 
**i_ezsigntemplatedocumentpage_pagenumber** | **int** | The page number in the Ezsigntemplatedocument | 
**i_ezsigntemplatesignature_x** | **int** | The X coordinate (Horizontal) where to put the Ezsigntemplatesignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsigntemplatesignature 2 inches from the left border of the page, you would use \&quot;200\&quot; for the X coordinate. | 
**i_ezsigntemplatesignature_y** | **int** | The Y coordinate (Vertical) where to put the Ezsigntemplatesignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsigntemplatesignature 3 inches from the top border of the page, you would use \&quot;300\&quot; for the Y coordinate. | 
**i_ezsigntemplatesignature_width** | **int** | The width of the Ezsigntemplatesignature.  Size is calculated at 100dpi (dot per inch). So for example, if you want the Ezsigntemplatesignature to have a width of 2 inches, you would use \&quot;200\&quot; for the iEzsigntemplatesignatureWidth. | [optional] 
**i_ezsigntemplatesignature_height** | **int** | The height of the Ezsigntemplatesignature.  Size is calculated at 100dpi (dot per inch). So for example, if you want the Ezsigntemplatesignature to have an height of 2 inches, you would use \&quot;200\&quot; for the iEzsigntemplatesignatureHeight. | [optional] 
**i_ezsigntemplatesignature_step** | **int** | The step when the Ezsigntemplatesigner will be invited to sign | 
**e_ezsigntemplatesignature_type** | [**FieldEEzsigntemplatesignatureType**](FieldEEzsigntemplatesignatureType.md) |  | 
**t_ezsigntemplatesignature_tooltip** | **str** | A tooltip that will be presented to Ezsigntemplatesigner about the Ezsigntemplatesignature | [optional] 
**e_ezsigntemplatesignature_tooltipposition** | [**FieldEEzsigntemplatesignatureTooltipposition**](FieldEEzsigntemplatesignatureTooltipposition.md) |  | [optional] 
**e_ezsigntemplatesignature_font** | [**FieldEEzsigntemplatesignatureFont**](FieldEEzsigntemplatesignatureFont.md) |  | [optional] 
**i_ezsigntemplatesignature_validationstep** | **int** | The step when the Ezsigntemplatesigner will be invited to validate the Ezsigntemplatesignature of eEzsigntemplatesignatureType Attachments | [optional] 
**s_ezsigntemplatesignature_attachmentdescription** | **str** | The description attached to the attachment name added in Ezsigntemplatesignature of eEzsigntemplatesignatureType Attachments | [optional] 
**e_ezsigntemplatesignature_attachmentnamesource** | [**FieldEEzsigntemplatesignatureAttachmentnamesource**](FieldEEzsigntemplatesignatureAttachmentnamesource.md) |  | [optional] 
**b_ezsigntemplatesignature_required** | **bool** | Whether the Ezsigntemplatesignature is required or not. This field is relevant only with Ezsigntemplatesignature with eEzsigntemplatesignatureType &#x3D; Attachments. | [optional] 
**i_ezsigntemplatesignature_maxlength** | **int** | The maximum length for the value in the Ezsigntemplatesignature  This can only be set if eEzsigntemplatesignatureType is **FieldText** or **FieldTextarea** | [optional] 
**s_ezsigntemplatesignature_regexp** | **str** | A regular expression to indicate what values are acceptable for the Ezsigntemplatesignature.  This can only be set if eEzsigntemplatesignatureType is **Text** or **Textarea** | [optional] 
**e_ezsigntemplatesignature_textvalidation** | [**EnumTextvalidation**](EnumTextvalidation.md) |  | [optional] 
**e_ezsigntemplatesignature_dependencyrequirement** | [**FieldEEzsigntemplatesignatureDependencyrequirement**](FieldEEzsigntemplatesignatureDependencyrequirement.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_response import EzsigntemplatesignatureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureResponse from a JSON string
ezsigntemplatesignature_response_instance = EzsigntemplatesignatureResponse.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatesignatureResponse.to_json()

# convert the object into a dict
ezsigntemplatesignature_response_dict = ezsigntemplatesignature_response_instance.to_dict()
# create an instance of EzsigntemplatesignatureResponse from a dict
ezsigntemplatesignature_response_form_dict = ezsigntemplatesignature_response.from_dict(ezsigntemplatesignature_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


