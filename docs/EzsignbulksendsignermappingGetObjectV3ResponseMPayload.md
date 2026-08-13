# EzsignbulksendsignermappingGetObjectV3ResponseMPayload

Payload for GET /3/object/ezsignbulksendsignermapping/{pkiEzsignbulksendsignermappingID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignbulksendsignermapping** | [**EzsignbulksendsignermappingResponseCompoundV3**](EzsignbulksendsignermappingResponseCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendsignermapping_get_object_v3_response_m_payload import EzsignbulksendsignermappingGetObjectV3ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendsignermappingGetObjectV3ResponseMPayload from a JSON string
ezsignbulksendsignermapping_get_object_v3_response_m_payload_instance = EzsignbulksendsignermappingGetObjectV3ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendsignermappingGetObjectV3ResponseMPayload.to_json())

# convert the object into a dict
ezsignbulksendsignermapping_get_object_v3_response_m_payload_dict = ezsignbulksendsignermapping_get_object_v3_response_m_payload_instance.to_dict()
# create an instance of EzsignbulksendsignermappingGetObjectV3ResponseMPayload from a dict
ezsignbulksendsignermapping_get_object_v3_response_m_payload_from_dict = EzsignbulksendsignermappingGetObjectV3ResponseMPayload.from_dict(ezsignbulksendsignermapping_get_object_v3_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


