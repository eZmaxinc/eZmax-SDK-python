# EzsigndocumentResponseCompound

An Ezsigndocument Object and children to create a complete structure
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**dt_ezsigndocument_duedate** | **str** | The maximum date and time at which the document can be signed. | 
**fki_language_id** | [**FieldPkiLanguageID**](FieldPkiLanguageID.md) |  | 
**s_ezsigndocument_filename** | **str** | The actual file name that will be used when downloading or attaching to an email. | 
**s_ezsigndocument_name** | **str** | The name of the document that will be presented to Ezsignfoldersignerassociations | 
**pki_ezsigndocument_id** | **int** | The unique ID of the Ezsigntemplate | 
**e_ezsigndocument_step** | [**FieldEEzsigndocumentStep**](FieldEEzsigndocumentStep.md) |  | 
**dt_ezsigndocument_firstsend** | **str** | The date and time when the Ezsigndocument was first sent. | 
**dt_ezsigndocument_lastsend** | **str** | The date and time when the Ezsigndocument was sent the last time. | 
**i_ezsigndocument_order** | **int** | The order in which the Ezsigndocument will be presented to the signatory in the Ezsignfolder. | 
**i_ezsigndocument_pagetotal** | **int** | The number of pages in the Ezsigndocument. | 
**i_ezsigndocument_signaturesigned** | **int** | The number of signatures that were signed in the document. | 
**i_ezsigndocument_signaturetotal** | **int** | The number of total signatures that were requested in the Ezsigndocument. | 
**s_ezsigndocument_md5initial** | **str** | MD5 Hash of the initial PDF Document before signatures were applied to it. | 
**s_ezsigndocument_md5signed** | **str** | MD5 Hash of the final PDF Document after all signatures were applied to it. | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

