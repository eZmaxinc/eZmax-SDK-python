# EzsigndocumentRequest

An Ezsigndocument Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsignfolder_id** | **int** | A reference to a valid Ezsignfolder.  That value is returned after a successful Ezsignfolder Creation. | 
**dt_ezsigndocument_duedate** | **str** | Represent a Date Time. The timezone is the one configured in the User&#39;s profile. | 
**fki_language_id** | [**FieldPkiLanguageID**](FieldPkiLanguageID.md) |  | 
**s_ezsigndocument_name** | **str** | The name of the document that will be presented to Ezsignfoldersignerassociations | 
**e_ezsigndocument_source** | **str** | Indicates where to look for the document binary content. | defaults to "Base64"
**e_ezsigndocument_format** | **str** | Indicates the format of the document. | defaults to "Pdf"
**s_ezsigndocument_base64** | **str** | The Base64 encoded binary content of the document.  This field is Required when eEzsigndocumentSource &#x3D; Base64. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


