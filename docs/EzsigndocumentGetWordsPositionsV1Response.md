# EzsigndocumentGetWordsPositionsV1Response

Response for POST /1/object/ezsigndocument/{pkiEzsigndocumentID}/getWordsPositions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**List[CustomWordPositionWordResponse]**](CustomWordPositionWordResponse.md) | Payload for POST /1/object/ezsigndocument/{pkiEzsigndocumentID}/getWordsPositions | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_words_positions_v1_response import EzsigndocumentGetWordsPositionsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetWordsPositionsV1Response from a JSON string
ezsigndocument_get_words_positions_v1_response_instance = EzsigndocumentGetWordsPositionsV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetWordsPositionsV1Response.to_json())

# convert the object into a dict
ezsigndocument_get_words_positions_v1_response_dict = ezsigndocument_get_words_positions_v1_response_instance.to_dict()
# create an instance of EzsigndocumentGetWordsPositionsV1Response from a dict
ezsigndocument_get_words_positions_v1_response_from_dict = EzsigndocumentGetWordsPositionsV1Response.from_dict(ezsigndocument_get_words_positions_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


