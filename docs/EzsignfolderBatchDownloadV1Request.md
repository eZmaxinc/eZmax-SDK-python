# EzsignfolderBatchDownloadV1Request

Request for POST /1/object/ezsignfolder/{pkiEzsignfolderID}/batchDownload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsigndocument_id** | **[int]** |  | 
**a_e_document_type** | **[str]** | The type of document to retrieve.  1. **Signed** Is the final document once all signatures were applied. 2. **Proofdocument** Is the evidence report. 3. **Proof** Is the complete evidence archive including all of the above and more. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


