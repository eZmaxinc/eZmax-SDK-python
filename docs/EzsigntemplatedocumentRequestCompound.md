# EzsigntemplatedocumentRequestCompound

A Ezsigntemplatedocument Object and children

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**s_ezsigntemplatedocument_name** | **str** | The name of the Ezsigntemplatedocument. | 
**e_ezsigntemplatedocument_source** | **str** | Indicates where to look for the document binary content. | 
**pki_ezsigntemplatedocument_id** | **int** | The unique ID of the Ezsigntemplatedocument | [optional] 
**fki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | [optional] 
**fki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | [optional] 
**e_ezsigntemplatedocument_format** | **str** | Indicates the format of the template. | [optional]  if omitted the server will use the default value of "Pdf"
**s_ezsigntemplatedocument_base64** | **str** | The Base64 encoded binary content of the document.  This field is Required when eEzsigntemplatedocumentSource &#x3D; Base64. | [optional] 
**s_ezsigntemplatedocument_url** | **str** | The url where the document content resides.  This field is Required when eEzsigntemplatedocumentSource &#x3D; Url. | [optional] 
**b_ezsigntemplatedocument_forcerepair** | **bool** | Try to repair the document or flatten it if it cannot be used for electronic signature. | [optional] 
**e_ezsigntemplatedocument_form** | **str** | If the document contains an existing PDF form this property must be set.  **Keep** leaves the form as-is in the document.  **Convert** removes the form and convert all the existing fields to Ezsigntemplateformfieldgroups and assign them to the specified **fkiEzsigntemplatesignerID** | [optional] 
**s_ezsigntemplatedocument_password** | **str** | If the source template is password protected, the password to open/modify it. | [optional]  if omitted the server will use the default value of ""
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


