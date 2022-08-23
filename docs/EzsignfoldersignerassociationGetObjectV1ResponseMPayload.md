# EzsignfoldersignerassociationGetObjectV1ResponseMPayload

Payload for GET /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfoldersignerassociation_id** | [**FieldPkiEzsignfoldersignerassociationID**](FieldPkiEzsignfoldersignerassociationID.md) |  | 
**fki_ezsignfolder_id** | [**FieldPkiEzsignfolderID**](FieldPkiEzsignfolderID.md) |  | 
**b_ezsignfoldersignerassociation_receivecopy** | **bool** | If this flag is true. The signatory will receive a copy of every signed Ezsigndocument even if it ain&#39;t required to sign the document. | 
**t_ezsignfoldersignerassociation_message** | **str** | A custom text message that will be added to the email sent. | 
**obj_user** | [**EzsignfoldersignerassociationResponseCompoundUser**](EzsignfoldersignerassociationResponseCompoundUser.md) |  | [optional] 
**obj_ezsignsigner** | [**EzsignsignerResponseCompound**](EzsignsignerResponseCompound.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


