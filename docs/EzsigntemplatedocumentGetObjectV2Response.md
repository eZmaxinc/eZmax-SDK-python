# EzsigntemplatedocumentGetObjectV2Response

Response for GET /2/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsigntemplatedocumentGetObjectV2ResponseMPayload**](EzsigntemplatedocumentGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_get_object_v2_response import EzsigntemplatedocumentGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentGetObjectV2Response from a JSON string
ezsigntemplatedocument_get_object_v2_response_instance = EzsigntemplatedocumentGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentGetObjectV2Response.to_json())

# convert the object into a dict
ezsigntemplatedocument_get_object_v2_response_dict = ezsigntemplatedocument_get_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentGetObjectV2Response from a dict
ezsigntemplatedocument_get_object_v2_response_from_dict = EzsigntemplatedocumentGetObjectV2Response.from_dict(ezsigntemplatedocument_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


