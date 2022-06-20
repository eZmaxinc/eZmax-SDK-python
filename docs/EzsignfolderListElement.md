# EzsignfolderListElement

An Ezsignfolder List Element

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfolder_id** | [**FieldPkiEzsignfolderID**](FieldPkiEzsignfolderID.md) |  | 
**fki_ezsignfoldertype_id** | [**FieldPkiEzsignfoldertypeID**](FieldPkiEzsignfoldertypeID.md) |  | 
**e_ezsignfoldertype_privacylevel** | [**FieldEEzsignfoldertypePrivacylevel**](FieldEEzsignfoldertypePrivacylevel.md) |  | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | 
**s_ezsignfolder_description** | **str** | The description of the Ezsignfolder | 
**e_ezsignfolder_step** | [**FieldEEzsignfolderStep**](FieldEEzsignfolderStep.md) |  | 
**dt_created_date** | **str** | The date and time at which the object was created | 
**i_ezsigndocument** | **int** | The total number of Ezsigndocument in the folder | 
**i_ezsigndocument_edm** | **int** | The total number of Ezsigndocument in the folder that were saved in the edm system | 
**i_ezsignsignature** | **int** | The total number of signature blocks in all Ezsigndocuments in the folder | 
**i_ezsignsignature_signed** | **int** | The total number of already signed signature blocks in all Ezsigndocuments in the folder | 
**dt_ezsignfolder_sentdate** | **str** | The date and time at which the Ezsign folder was sent the last time. | [optional] 
**dt_ezsignfolder_duedate** | **str** | The maximum date and time at which the Ezsignfolder can be signed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


