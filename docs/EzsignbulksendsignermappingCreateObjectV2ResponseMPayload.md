# EzsignbulksendsignermappingCreateObjectV2ResponseMPayload

Payload for POST /2/object/ezsignbulksendsignermapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsignbulksendsignermapping_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.ezsignbulksendsignermapping_create_object_v2_response_m_payload import EzsignbulksendsignermappingCreateObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendsignermappingCreateObjectV2ResponseMPayload from a JSON string
ezsignbulksendsignermapping_create_object_v2_response_m_payload_instance = EzsignbulksendsignermappingCreateObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendsignermappingCreateObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsignbulksendsignermapping_create_object_v2_response_m_payload_dict = ezsignbulksendsignermapping_create_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignbulksendsignermappingCreateObjectV2ResponseMPayload from a dict
ezsignbulksendsignermapping_create_object_v2_response_m_payload_from_dict = EzsignbulksendsignermappingCreateObjectV2ResponseMPayload.from_dict(ezsignbulksendsignermapping_create_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


