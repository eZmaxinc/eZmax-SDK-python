# EzsigntemplateformfieldgroupGetObjectV1ResponseMPayload

Payload for GET /1/object/ezsigntemplateformfieldgroup/{pkiEzsigntemplateformfieldgroupID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateformfieldgroup_id** | [**FieldPkiEzsigntemplateformfieldgroupID**](FieldPkiEzsigntemplateformfieldgroupID.md) |  | 
**fki_ezsigntemplatedocument_id** | [**FieldPkiEzsigntemplatedocumentID**](FieldPkiEzsigntemplatedocumentID.md) |  | 
**e_ezsigntemplateformfieldgroup_type** | [**FieldEEzsigntemplateformfieldgroupType**](FieldEEzsigntemplateformfieldgroupType.md) |  | 
**e_ezsigntemplateformfieldgroup_signerrequirement** | [**FieldEEzsigntemplateformfieldgroupSignerrequirement**](FieldEEzsigntemplateformfieldgroupSignerrequirement.md) |  | 
**s_ezsigntemplateformfieldgroup_label** | **str** | The Label for the Ezsigntemplateformfieldgroup | 
**i_ezsigntemplateformfieldgroup_step** | [**FieldIEzsigntemplateformfieldgroupStep**](FieldIEzsigntemplateformfieldgroupStep.md) |  | 
**i_ezsigntemplateformfieldgroup_filledmin** | [**FieldIEzsigntemplateformfieldgroupFilledmin**](FieldIEzsigntemplateformfieldgroupFilledmin.md) |  | 
**i_ezsigntemplateformfieldgroup_filledmax** | [**FieldIEzsigntemplateformfieldgroupFilledmax**](FieldIEzsigntemplateformfieldgroupFilledmax.md) |  | 
**b_ezsigntemplateformfieldgroup_readonly** | **bool** | Whether the Ezsigntemplateformfieldgroup is read only or not. | 
**a_obj_ezsigntemplateformfieldgroupsigner** | [**[EzsigntemplateformfieldgroupsignerResponseCompound]**](EzsigntemplateformfieldgroupsignerResponseCompound.md) |  | 
**a_obj_ezsigntemplateformfield** | [**[EzsigntemplateformfieldResponseCompound]**](EzsigntemplateformfieldResponseCompound.md) |  | 
**s_ezsigntemplateformfieldgroup_defaultvalue** | **str** | The default value for the Ezsigntemplateformfieldgroup | [optional] 
**i_ezsigntemplateformfieldgroup_maxlength** | [**FieldIEzsigntemplateformfieldgroupMaxlength**](FieldIEzsigntemplateformfieldgroupMaxlength.md) |  | [optional] 
**b_ezsigntemplateformfieldgroup_encrypted** | **bool** | Whether the Ezsigntemplateformfieldgroup is encrypted in the database or not. Encrypted values are not displayed on the Ezsigndocument. This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea** | [optional] 
**s_ezsigntemplateformfieldgroup_regexp** | **str** | A regular expression to indicate what values are acceptable for the Ezsigntemplateformfieldgroup.  This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea** | [optional] 
**t_ezsigntemplateformfieldgroup_tooltip** | **str** | A tooltip that will be presented to Ezsigntemplatesigner about the Ezsigntemplateformfieldgroup | [optional] 
**e_ezsigntemplateformfieldgroup_tooltipposition** | [**FieldEEzsigntemplateformfieldgroupTooltipposition**](FieldEEzsigntemplateformfieldgroupTooltipposition.md) |  | [optional] 
**a_obj_dropdown_element** | [**[CustomDropdownElementResponseCompound]**](CustomDropdownElementResponseCompound.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


