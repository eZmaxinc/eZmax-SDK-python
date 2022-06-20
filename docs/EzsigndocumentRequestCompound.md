# EzsigndocumentRequestCompound

An Ezsigndocument Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsignfolder_id** | [**FieldPkiEzsignfolderID**](FieldPkiEzsignfolderID.md) |  | 
**fki_language_id** | [**FieldPkiLanguageID**](FieldPkiLanguageID.md) |  | 
**e_ezsigndocument_source** | **str** | Indicates where to look for the document binary content. | 
**dt_ezsigndocument_duedate** | **str** | The maximum date and time at which the Ezsigndocument can be signed. | 
**s_ezsigndocument_name** | **str** | The name of the document that will be presented to Ezsignfoldersignerassociations | 
**pki_ezsigndocument_id** | [**FieldPkiEzsigndocumentID**](FieldPkiEzsigndocumentID.md) |  | [optional] 
**fki_ezsigntemplate_id** | [**FieldPkiEzsigntemplateID**](FieldPkiEzsigntemplateID.md) |  | [optional] 
**fki_ezsignfoldersignerassociation_id** | [**FieldPkiEzsignfoldersignerassociationID**](FieldPkiEzsignfoldersignerassociationID.md) |  | [optional] 
**e_ezsigndocument_format** | **str** | Indicates the format of the document. | [optional]  if omitted the server will use the default value of "Pdf"
**s_ezsigndocument_base64** | **str** | The Base64 encoded binary content of the document.  This field is Required when eEzsigndocumentSource &#x3D; Base64. | [optional] 
**s_ezsigndocument_url** | **str** | The url where the document content resides.  This field is Required when eEzsigndocumentSource &#x3D; Url. | [optional] 
**b_ezsigndocument_forcerepair** | **bool** | Try to repair the document or flatten it if it cannot be used for electronic signature.  | [optional]  if omitted the server will use the default value of True
**s_ezsigndocument_password** | **str** | If the source document is password protected, the password to open/modify it. | [optional] 
**e_ezsigndocument_form** | **str** | If the document contains an existing PDF form this property must be set.  **Keep** leaves the form as-is in the document.  **Convert** removes the form and convert all the existing fields to Ezsignformfieldgroups and assign them to the specified **fkiEzsignfoldersignerassociationID** | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


