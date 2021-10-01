# EzsigndocumentGetWordsPositionsV1Request

Request for the /1/object/ezsigndocument/{pkiEzsigndocumentID}/getWordsPositions API Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_get** | **str** | Specify if you want to retrieve *All* words or specific *Words* from the document. If you specify *Words*, you must send the list of words to search in *a_sWord*. | [optional] 
**a_s_word** | **[str]** | Array of words to find in the document | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


