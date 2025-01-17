# EzsigntemplatedocumentpagerecognitionCreateObjectV1Response

Response for POST /1/object/ezsigntemplatedocumentpagerecognition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsigntemplatedocumentpagerecognitionCreateObjectV1ResponseMPayload**](EzsigntemplatedocumentpagerecognitionCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocumentpagerecognition_create_object_v1_response import EzsigntemplatedocumentpagerecognitionCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentpagerecognitionCreateObjectV1Response from a JSON string
ezsigntemplatedocumentpagerecognition_create_object_v1_response_instance = EzsigntemplatedocumentpagerecognitionCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentpagerecognitionCreateObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplatedocumentpagerecognition_create_object_v1_response_dict = ezsigntemplatedocumentpagerecognition_create_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentpagerecognitionCreateObjectV1Response from a dict
ezsigntemplatedocumentpagerecognition_create_object_v1_response_from_dict = EzsigntemplatedocumentpagerecognitionCreateObjectV1Response.from_dict(ezsigntemplatedocumentpagerecognition_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


