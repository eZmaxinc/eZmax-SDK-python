# EzsigndocumentGetObjectV1ResponseMPayload

Payload for GET /1/object/ezsigndocument/{pkiEzsigndocumentID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsignfolder_id** | [**FieldPkiEzsignfolderID**](FieldPkiEzsignfolderID.md) |  | 
**dt_ezsigndocument_duedate** | **str** | The maximum date and time at which the Ezsigndocument can be signed. | 
**fki_language_id** | [**FieldPkiLanguageID**](FieldPkiLanguageID.md) |  | 
**s_ezsigndocument_name** | **str** | The name of the document that will be presented to Ezsignfoldersignerassociations | 
**pki_ezsigndocument_id** | [**FieldPkiEzsigndocumentID**](FieldPkiEzsigndocumentID.md) |  | 
**e_ezsigndocument_step** | [**FieldEEzsigndocumentStep**](FieldEEzsigndocumentStep.md) |  | 
**i_ezsigndocument_order** | [**FieldIEzsigndocumentOrder**](FieldIEzsigndocumentOrder.md) |  | 
**i_ezsigndocument_pagetotal** | [**FieldIEzsigndocumentPagetotal**](FieldIEzsigndocumentPagetotal.md) |  | 
**i_ezsigndocument_signaturesigned** | [**FieldIEzsigndocumentSignaturesigned**](FieldIEzsigndocumentSignaturesigned.md) |  | 
**i_ezsigndocument_signaturetotal** | [**FieldIEzsigndocumentSignaturetotal**](FieldIEzsigndocumentSignaturetotal.md) |  | 
**s_ezsigndocument_md5initial** | **str** | MD5 Hash of the initial PDF Document before signatures were applied to it. | 
**s_ezsigndocument_md5signed** | **str** | MD5 Hash of the final PDF Document after all signatures were applied to it. | 
**b_ezsigndocument_ezsignform** | **bool** | If the Ezsigndocument contains an Ezsignform or not | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 
**i_ezsigndocument_stepformtotal** | **int** | The total number of steps in the form filling phase | 
**i_ezsigndocument_stepformcurrent** | **int** | The current step in the form filling phase | 
**i_ezsigndocument_stepsignaturetotal** | **int** | The total number of steps in the signature filling phase | 
**i_ezsigndocument_stepsignature_current** | **int** | The current step in the signature phase | 
**a_obj_ezsignfoldersignerassociationstatus** | [**[CustomEzsignfoldersignerassociationstatusResponse]**](CustomEzsignfoldersignerassociationstatusResponse.md) |  | 
**dt_ezsigndocument_firstsend** | **str** | The date and time when the Ezsigndocument was first sent. | [optional] 
**dt_ezsigndocument_lastsend** | **str** | The date and time when the Ezsigndocument was sent the last time. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


