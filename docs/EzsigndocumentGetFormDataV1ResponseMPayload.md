# EzsigndocumentGetFormDataV1ResponseMPayload

Payload for the /1/object/ezsigndocument/{pkiEzsigndocument}/getFormData API Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | 
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**s_ezsigndocument_name** | **str** | The name of the document that will be presented to Ezsignfoldersignerassociations | 
**dt_modified_date** | **str** | The date and time at which the object was last modified | 
**a_obj_form_data_signer** | [**[CustomFormDataSignerResponse]**](CustomFormDataSignerResponse.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


