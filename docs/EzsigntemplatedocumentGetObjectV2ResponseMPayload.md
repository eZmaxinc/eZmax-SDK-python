# EzsigntemplatedocumentGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatedocument** | [**EzsigntemplatedocumentResponseCompound**](EzsigntemplatedocumentResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_get_object_v2_response_m_payload import EzsigntemplatedocumentGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentGetObjectV2ResponseMPayload from a JSON string
ezsigntemplatedocument_get_object_v2_response_m_payload_instance = EzsigntemplatedocumentGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatedocument_get_object_v2_response_m_payload_dict = ezsigntemplatedocument_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatedocumentGetObjectV2ResponseMPayload from a dict
ezsigntemplatedocument_get_object_v2_response_m_payload_form_dict = ezsigntemplatedocument_get_object_v2_response_m_payload.from_dict(ezsigntemplatedocument_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


