# EzsigndocumentExtractTextV1ResponseMPayload

Response for POST /1/object/ezsigndocument/{pkiEzsigndocumentID}/ExtractText

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_text** | **str** | The text extract from document | 

## Example

```python
from eZmaxApi.models.ezsigndocument_extract_text_v1_response_m_payload import EzsigndocumentExtractTextV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentExtractTextV1ResponseMPayload from a JSON string
ezsigndocument_extract_text_v1_response_m_payload_instance = EzsigndocumentExtractTextV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentExtractTextV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigndocument_extract_text_v1_response_m_payload_dict = ezsigndocument_extract_text_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigndocumentExtractTextV1ResponseMPayload from a dict
ezsigndocument_extract_text_v1_response_m_payload_from_dict = EzsigndocumentExtractTextV1ResponseMPayload.from_dict(ezsigndocument_extract_text_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


