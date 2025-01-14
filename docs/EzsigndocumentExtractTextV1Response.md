# EzsigndocumentExtractTextV1Response

Response for POST /1/object/ezsigndocument/{pkiEzsigndocumentID}/extractText

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigndocumentExtractTextV1ResponseMPayload**](EzsigndocumentExtractTextV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_extract_text_v1_response import EzsigndocumentExtractTextV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentExtractTextV1Response from a JSON string
ezsigndocument_extract_text_v1_response_instance = EzsigndocumentExtractTextV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentExtractTextV1Response.to_json())

# convert the object into a dict
ezsigndocument_extract_text_v1_response_dict = ezsigndocument_extract_text_v1_response_instance.to_dict()
# create an instance of EzsigndocumentExtractTextV1Response from a dict
ezsigndocument_extract_text_v1_response_from_dict = EzsigndocumentExtractTextV1Response.from_dict(ezsigndocument_extract_text_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


