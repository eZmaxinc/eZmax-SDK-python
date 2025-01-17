# EzsigntemplatedocumentpagerecognitionGetObjectV2Response

Response for GET /2/object/ezsigntemplatedocumentpagerecognition/{pkiEzsigntemplatedocumentpagerecognitionID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsigntemplatedocumentpagerecognitionGetObjectV2ResponseMPayload**](EzsigntemplatedocumentpagerecognitionGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocumentpagerecognition_get_object_v2_response import EzsigntemplatedocumentpagerecognitionGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentpagerecognitionGetObjectV2Response from a JSON string
ezsigntemplatedocumentpagerecognition_get_object_v2_response_instance = EzsigntemplatedocumentpagerecognitionGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentpagerecognitionGetObjectV2Response.to_json())

# convert the object into a dict
ezsigntemplatedocumentpagerecognition_get_object_v2_response_dict = ezsigntemplatedocumentpagerecognition_get_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentpagerecognitionGetObjectV2Response from a dict
ezsigntemplatedocumentpagerecognition_get_object_v2_response_from_dict = EzsigntemplatedocumentpagerecognitionGetObjectV2Response.from_dict(ezsigntemplatedocumentpagerecognition_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


