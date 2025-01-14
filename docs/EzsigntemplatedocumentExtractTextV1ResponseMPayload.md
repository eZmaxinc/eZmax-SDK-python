# EzsigntemplatedocumentExtractTextV1ResponseMPayload

Response for POST /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/ExtractText

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_text** | **str** | The text extract from document | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_extract_text_v1_response_m_payload import EzsigntemplatedocumentExtractTextV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentExtractTextV1ResponseMPayload from a JSON string
ezsigntemplatedocument_extract_text_v1_response_m_payload_instance = EzsigntemplatedocumentExtractTextV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentExtractTextV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatedocument_extract_text_v1_response_m_payload_dict = ezsigntemplatedocument_extract_text_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatedocumentExtractTextV1ResponseMPayload from a dict
ezsigntemplatedocument_extract_text_v1_response_m_payload_from_dict = EzsigntemplatedocumentExtractTextV1ResponseMPayload.from_dict(ezsigntemplatedocument_extract_text_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


