# EzsignfolderRequestCompound

An Ezsignfolder Object and children to create a complete structure
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_ezsignfoldersignerassociation** | [**[EzsignfoldersignerassociationRequest]**](EzsignfoldersignerassociationRequest.md) | An array of signers that will be invited to sign the Ezsigndocuments | 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype.    This value can be queried by the API and is also visible in the admin interface.    There are two types of Ezsignfoldertype. **User** and **Shared**. **User** can only be seen by the user who created the folder or its assistants. Access to **Shared** folders are configurable for access and email delivery. You should typically choose a **Shared** type here. | 
**fki_ezsigntsarequirement_id** | [**FieldPkiEzsigntsarequirementID**](FieldPkiEzsigntsarequirementID.md) |  | 
**s_ezsignfolder_description** | **str** | The description of the Ezsign Folder | 
**t_ezsignfolder_note** | **str** | Somes extra notes about the eZsign Folder | 
**e_ezsignfolder_sendreminderfrequency** | [**FieldEEzsignfolderSendreminderfrequency**](FieldEEzsignfolderSendreminderfrequency.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

