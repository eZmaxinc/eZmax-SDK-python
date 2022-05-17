# EzsigndocumentGetWordsPositionsV1Request

Request for POST /1/object/ezsigndocument/{pkiEzsigndocumentID}/getWordsPositions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_get** | **str** | Specify if you want to retrieve *All* words or specific *Words* from the document. If you specify *Words*, you must send the list of words to search for in *a_sWord*. | 
**b_word_case_sensitive** | **bool** | IF *true*, words will be searched case-sensitive and results will be returned case-sensitive. IF *false*, words will be searched case-insensitive and results will be returned case-insensitive. | 
**a_s_word** | **[str]** | Array of words to find in the document | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


