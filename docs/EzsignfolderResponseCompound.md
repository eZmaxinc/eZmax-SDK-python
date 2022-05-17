# EzsignfolderResponseCompound

An Ezsignfolder Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | 
**fki_billingentityinternal_id** | **int** | The unique ID of the Billingentityinternal. | 
**s_billingentityinternal_description_x** | **str** | The description of the Billingentityinternal in the language of the requester | 
**fki_ezsigntsarequirement_id** | [**FieldPkiEzsigntsarequirementID**](FieldPkiEzsigntsarequirementID.md) |  | 
**s_ezsigntsarequirement_description_x** | **str** | The description of the Ezsigntsarequirement in the language of the requester | 
**s_ezsignfolder_description** | **str** | The description of the Ezsignfolder | 
**t_ezsignfolder_note** | **str** | Note about the Ezsignfolder | 
**e_ezsignfolder_sendreminderfrequency** | [**FieldEEzsignfolderSendreminderfrequency**](FieldEEzsignfolderSendreminderfrequency.md) |  | 
**dt_ezsignfolder_scheduledarchive** | **str** | The scheduled date and time at which the Ezsignfolder should be archived. | 
**dt_ezsignfolder_scheduleddestruction** | **str** | The scheduled date and time at which the Ezsignfolder should be Destroyed. | 
**e_ezsignfolder_step** | [**FieldEEzsignfolderStep**](FieldEEzsignfolderStep.md) |  | 
**dt_ezsignfolder_close** | **str** | The date and time at which the folder was closed. Either by applying the last signature or by completing it prematurely. | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 
**dt_ezsignfolder_duedate** | **str** | The maximum date and time at which the Ezsignfolder can be signed. | [optional] 
**dt_ezsignfolder_sentdate** | **str** | The date and time at which the Ezsign folder was sent the last time. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


