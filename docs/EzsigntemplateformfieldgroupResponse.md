# EzsigntemplateformfieldgroupResponse

A Ezsigntemplateformfieldgroup Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateformfieldgroup_id** | **int** | The unique ID of the Ezsigntemplateformfieldgroup | 
**fki_ezsigntemplatedocument_id** | **int** | The unique ID of the Ezsigntemplatedocument | 
**e_ezsigntemplateformfieldgroup_type** | [**FieldEEzsigntemplateformfieldgroupType**](FieldEEzsigntemplateformfieldgroupType.md) |  | 
**e_ezsigntemplateformfieldgroup_signerrequirement** | [**FieldEEzsigntemplateformfieldgroupSignerrequirement**](FieldEEzsigntemplateformfieldgroupSignerrequirement.md) |  | 
**s_ezsigntemplateformfieldgroup_label** | **str** | The Label for the Ezsigntemplateformfieldgroup | 
**i_ezsigntemplateformfieldgroup_step** | **int** | The step when the Ezsigntemplatesigner will be invited to fill the form fields | 
**s_ezsigntemplateformfieldgroup_defaultvalue** | **str** | The default value for the Ezsigntemplateformfieldgroup | 
**i_ezsigntemplateformfieldgroup_filledmin** | **int** | The minimum number of Ezsigntemplateformfield that must be filled in the Ezsigntemplateformfieldgroup | 
**i_ezsigntemplateformfieldgroup_filledmax** | **int** | The maximum number of Ezsigntemplateformfield that must be filled in the Ezsigntemplateformfieldgroup | 
**b_ezsigntemplateformfieldgroup_readonly** | **bool** | Whether the Ezsigntemplateformfieldgroup is read only or not. | 
**i_ezsigntemplateformfieldgroup_maxlength** | **int** | The maximum length for the value in the Ezsigntemplateformfieldgroup  This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea** | [optional] 
**b_ezsigntemplateformfieldgroup_encrypted** | **bool** | Whether the Ezsigntemplateformfieldgroup is encrypted in the database or not. Encrypted values are not displayed on the Ezsigndocument. This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea** | [optional] 
**s_ezsigntemplateformfieldgroup_regexp** | **str** | A regular expression to indicate what values are acceptable for the Ezsigntemplateformfieldgroup.  This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea** | [optional] 
**t_ezsigntemplateformfieldgroup_tooltip** | **str** | A tooltip that will be presented to Ezsigntemplatesigner about the Ezsigntemplateformfieldgroup | [optional] 
**e_ezsigntemplateformfieldgroup_tooltipposition** | [**FieldEEzsigntemplateformfieldgroupTooltipposition**](FieldEEzsigntemplateformfieldgroupTooltipposition.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


