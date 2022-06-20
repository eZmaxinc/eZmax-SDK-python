# EzsignformfieldgroupResponse

An Ezsignformfieldgroup Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignformfieldgroup_id** | [**FieldPkiEzsignformfieldgroupID**](FieldPkiEzsignformfieldgroupID.md) |  | 
**fki_ezsigndocument_id** | [**FieldPkiEzsigndocumentID**](FieldPkiEzsigndocumentID.md) |  | 
**e_ezsignformfieldgroup_type** | [**FieldEEzsignformfieldgroupType**](FieldEEzsignformfieldgroupType.md) |  | 
**e_ezsignformfieldgroup_signerrequirement** | [**FieldEEzsignformfieldgroupSignerrequirement**](FieldEEzsignformfieldgroupSignerrequirement.md) |  | 
**s_ezsignformfieldgroup_label** | **str** | The Label for the Ezsignformfieldgroup | 
**i_ezsignformfieldgroup_step** | [**FieldIEzsignformfieldgroupStep**](FieldIEzsignformfieldgroupStep.md) |  | 
**s_ezsignformfieldgroup_defaultvalue** | **str** | The default value for the Ezsignformfieldgroup | 
**i_ezsignformfieldgroup_filledmin** | [**FieldIEzsignformfieldgroupFilledmin**](FieldIEzsignformfieldgroupFilledmin.md) |  | 
**i_ezsignformfieldgroup_filledmax** | [**FieldIEzsignformfieldgroupFilledmax**](FieldIEzsignformfieldgroupFilledmax.md) |  | 
**b_ezsignformfieldgroup_readonly** | **bool** | Whether the Ezsignformfieldgroup is read only or not. | 
**i_ezsignformfieldgroup_maxlength** | [**FieldIEzsignformfieldgroupMaxlength**](FieldIEzsignformfieldgroupMaxlength.md) |  | [optional] 
**b_ezsignformfieldgroup_encrypted** | **bool** | Whether the Ezsignformfieldgroup is encrypted in the database or not. Encrypted values are not displayed on the Ezsigndocument. This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea** | [optional] 
**s_ezsignformfieldgroup_regexp** | **str** | A regular expression to indicate what values are acceptable for the Ezsignformfieldgroup.  This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea** | [optional] 
**t_ezsignformfieldgroup_tooltip** | **str** | A tooltip that will be presented to Ezsignsigner about the Ezsignformfieldgroup | [optional] 
**e_ezsignformfieldgroup_tooltipposition** | [**FieldEEzsignformfieldgroupTooltipposition**](FieldEEzsignformfieldgroupTooltipposition.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


