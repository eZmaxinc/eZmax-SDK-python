# EzsigntemplatesignatureRequestCompound

A Ezsigntemplatesignature Object and children

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsigntemplatedocument_id** | [**FieldPkiEzsigntemplatedocumentID**](FieldPkiEzsigntemplatedocumentID.md) |  | 
**fki_ezsigntemplatesigner_id** | [**FieldPkiEzsigntemplatesignerID**](FieldPkiEzsigntemplatesignerID.md) |  | 
**i_ezsigntemplatedocumentpage_pagenumber** | [**FieldIEzsigntemplatedocumentpagePagenumber**](FieldIEzsigntemplatedocumentpagePagenumber.md) |  | 
**i_ezsigntemplatesignature_x** | [**FieldIEzsigntemplatesignatureX**](FieldIEzsigntemplatesignatureX.md) |  | 
**i_ezsigntemplatesignature_y** | [**FieldIEzsigntemplatesignatureY**](FieldIEzsigntemplatesignatureY.md) |  | 
**i_ezsigntemplatesignature_step** | [**FieldIEzsigntemplatesignatureStep**](FieldIEzsigntemplatesignatureStep.md) |  | 
**e_ezsigntemplatesignature_type** | [**FieldEEzsigntemplatesignatureType**](FieldEEzsigntemplatesignatureType.md) |  | 
**pki_ezsigntemplatesignature_id** | [**FieldPkiEzsigntemplatesignatureID**](FieldPkiEzsigntemplatesignatureID.md) |  | [optional] 
**t_ezsigntemplatesignature_tooltip** | **str** | A tooltip that will be presented to Ezsigntemplatesigner about the Ezsigntemplatesignature | [optional] 
**e_ezsigntemplatesignature_tooltipposition** | [**FieldEEzsigntemplatesignatureTooltipposition**](FieldEEzsigntemplatesignatureTooltipposition.md) |  | [optional] 
**e_ezsigntemplatesignature_font** | [**FieldEEzsigntemplatesignatureFont**](FieldEEzsigntemplatesignatureFont.md) |  | [optional] 
**b_ezsigntemplatesignature_customdate** | **bool** | Whether the Ezsigntemplatesignature has a custom date format or not. (Only possible when eEzsigntemplatesignatureType is **Name** or **Handwritten**) | [optional] 
**a_obj_ezsigntemplatesignaturecustomdate** | [**[EzsigntemplatesignaturecustomdateRequestCompound]**](EzsigntemplatesignaturecustomdateRequestCompound.md) | An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsigntemplatesignatureCustomdate is true.  Use an empty array if you don&#39;t want to have a date at all. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


