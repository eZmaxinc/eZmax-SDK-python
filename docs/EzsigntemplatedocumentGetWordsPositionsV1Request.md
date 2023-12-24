# EzsigntemplatedocumentGetWordsPositionsV1Request

Request for POST /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/getWordsPositions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_get** | **str** | Specify if you want to retrieve *All* words or specific *Words* from the document. If you specify *Words*, you must send the list of words to search for in *a_sWord*. | 
**b_word_case_sensitive** | **bool** | IF *true*, words will be searched case-sensitive and results will be returned case-sensitive. IF *false*, words will be searched case-insensitive and results will be returned case-insensitive. | 
**a_s_word** | **List[str]** | Array of words to find in the document | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_get_words_positions_v1_request import EzsigntemplatedocumentGetWordsPositionsV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentGetWordsPositionsV1Request from a JSON string
ezsigntemplatedocument_get_words_positions_v1_request_instance = EzsigntemplatedocumentGetWordsPositionsV1Request.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatedocumentGetWordsPositionsV1Request.to_json()

# convert the object into a dict
ezsigntemplatedocument_get_words_positions_v1_request_dict = ezsigntemplatedocument_get_words_positions_v1_request_instance.to_dict()
# create an instance of EzsigntemplatedocumentGetWordsPositionsV1Request from a dict
ezsigntemplatedocument_get_words_positions_v1_request_form_dict = ezsigntemplatedocument_get_words_positions_v1_request.from_dict(ezsigntemplatedocument_get_words_positions_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


