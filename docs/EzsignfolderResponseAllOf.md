# EzsignfolderResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype.    This value can be queried by the API and is also visible in the admin interface.    There are two types of Ezsignfoldertype. **User** and **Shared**. **User** can only be seen by the user who created the folder or its assistants. Access to **Shared** folders are configurable for access and email delivery. You should typically choose a **Shared** type here. | 
**fki_ezsigntsarequirement_id** | [**FieldPkiEzsigntsarequirementID**](FieldPkiEzsigntsarequirementID.md) |  | 
**s_ezsignfolder_description** | **str** | The description of the Ezsign Folder | 
**t_ezsignfolder_note** | **str** | Somes extra notes about the eZsign Folder | 
**e_ezsignfolder_sendreminderfrequency** | [**FieldEEzsignfolderSendreminderfrequency**](FieldEEzsignfolderSendreminderfrequency.md) |  | 
**pki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**dt_ezsignfolder_sentdate** | **str** | The date and time at which the Ezsign folder was sent the last time. | 
**e_ezsignfolder_step** | [**FieldEEzsignfolderStep**](FieldEEzsignfolderStep.md) |  | 
**dt_ezsignfolder_close** | **str** | The date and time at which the folder was closed. Either by applying the last signature or by completing it prematurely. | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


