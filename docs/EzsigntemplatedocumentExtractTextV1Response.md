# EzsigntemplatedocumentExtractTextV1Response

Response for POST /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/extractText

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatedocumentExtractTextV1ResponseMPayload**](EzsigntemplatedocumentExtractTextV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_extract_text_v1_response import EzsigntemplatedocumentExtractTextV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentExtractTextV1Response from a JSON string
ezsigntemplatedocument_extract_text_v1_response_instance = EzsigntemplatedocumentExtractTextV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentExtractTextV1Response.to_json())

# convert the object into a dict
ezsigntemplatedocument_extract_text_v1_response_dict = ezsigntemplatedocument_extract_text_v1_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentExtractTextV1Response from a dict
ezsigntemplatedocument_extract_text_v1_response_from_dict = EzsigntemplatedocumentExtractTextV1Response.from_dict(ezsigntemplatedocument_extract_text_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


