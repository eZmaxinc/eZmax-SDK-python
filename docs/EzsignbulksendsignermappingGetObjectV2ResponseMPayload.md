# EzsignbulksendsignermappingGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsignbulksendsignermapping/{pkiEzsignbulksendsignermappingID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignbulksendsignermapping** | [**EzsignbulksendsignermappingResponseCompound**](EzsignbulksendsignermappingResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendsignermapping_get_object_v2_response_m_payload import EzsignbulksendsignermappingGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendsignermappingGetObjectV2ResponseMPayload from a JSON string
ezsignbulksendsignermapping_get_object_v2_response_m_payload_instance = EzsignbulksendsignermappingGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignbulksendsignermappingGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
ezsignbulksendsignermapping_get_object_v2_response_m_payload_dict = ezsignbulksendsignermapping_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignbulksendsignermappingGetObjectV2ResponseMPayload from a dict
ezsignbulksendsignermapping_get_object_v2_response_m_payload_form_dict = ezsignbulksendsignermapping_get_object_v2_response_m_payload.from_dict(ezsignbulksendsignermapping_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


