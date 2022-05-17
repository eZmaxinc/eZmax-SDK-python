# EzsigntemplatesignatureGetObjectV1ResponseMPayload

Payload for GET /1/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatesignature_id** | **int** | The unique ID of the Ezsigntemplatesignature | 
**fki_ezsigntemplatedocument_id** | **int** | The unique ID of the Ezsigntemplatedocument | 
**fki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | 
**i_ezsigntemplatedocumentpage_pagenumber** | **int** | The page number in the Ezsigntemplatedocument | 
**i_ezsigntemplatesignature_x** | **int** | The X coordinate (Horizontal) where to put the Ezsigntemplatesignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsigntemplatesignature 2 inches from the left border of the page, you would use \&quot;200\&quot; for the X coordinate. | 
**i_ezsigntemplatesignature_y** | **int** | The Y coordinate (Vertical) where to put the Ezsigntemplatesignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsigntemplatesignature 3 inches from the top border of the page, you would use \&quot;300\&quot; for the Y coordinate. | 
**i_ezsigntemplatesignature_step** | **int** | The step when the Ezsigntemplatesigner will be invited to sign | 
**e_ezsigntemplatesignature_type** | [**FieldEEzsigntemplatesignatureType**](FieldEEzsigntemplatesignatureType.md) |  | 
**t_ezsigntemplatesignature_tooltip** | **str** | A tooltip that will be presented to Ezsigntemplatesigner about the Ezsigntemplatesignature | [optional] 
**e_ezsigntemplatesignature_tooltipposition** | [**FieldEEzsigntemplatesignatureTooltipposition**](FieldEEzsigntemplatesignatureTooltipposition.md) |  | [optional] 
**e_ezsigntemplatesignature_font** | [**FieldEEzsigntemplatesignatureFont**](FieldEEzsigntemplatesignatureFont.md) |  | [optional] 
**b_ezsigntemplatesignature_customdate** | **bool** | Whether the Ezsigntemplatesignature has a custom date format or not. (Only possible when eEzsigntemplatesignatureType is **Name** or **Handwritten**) | [optional] 
**a_obj_ezsigntemplatesignaturecustomdate** | [**[EzsigntemplatesignaturecustomdateResponseCompound]**](EzsigntemplatesignaturecustomdateResponseCompound.md) | An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsigntemplatesignatureCustomdate is true.  Use an empty array if you don&#39;t want to have a date at all. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


