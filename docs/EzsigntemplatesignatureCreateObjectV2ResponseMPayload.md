# EzsigntemplatesignatureCreateObjectV2ResponseMPayload

Payload for POST /2/object/ezsigntemplatesignature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsigntemplatesignature_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_create_object_v2_response_m_payload import EzsigntemplatesignatureCreateObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureCreateObjectV2ResponseMPayload from a JSON string
ezsigntemplatesignature_create_object_v2_response_m_payload_instance = EzsigntemplatesignatureCreateObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureCreateObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatesignature_create_object_v2_response_m_payload_dict = ezsigntemplatesignature_create_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatesignatureCreateObjectV2ResponseMPayload from a dict
ezsigntemplatesignature_create_object_v2_response_m_payload_from_dict = EzsigntemplatesignatureCreateObjectV2ResponseMPayload.from_dict(ezsigntemplatesignature_create_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


