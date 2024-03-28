# EzsignbulksenddocumentmappingGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsignbulksenddocumentmapping/{pkiEzsignbulksenddocumentmappingID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignbulksenddocumentmapping** | [**EzsignbulksenddocumentmappingResponseCompound**](EzsignbulksenddocumentmappingResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksenddocumentmapping_get_object_v2_response_m_payload import EzsignbulksenddocumentmappingGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksenddocumentmappingGetObjectV2ResponseMPayload from a JSON string
ezsignbulksenddocumentmapping_get_object_v2_response_m_payload_instance = EzsignbulksenddocumentmappingGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksenddocumentmappingGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsignbulksenddocumentmapping_get_object_v2_response_m_payload_dict = ezsignbulksenddocumentmapping_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignbulksenddocumentmappingGetObjectV2ResponseMPayload from a dict
ezsignbulksenddocumentmapping_get_object_v2_response_m_payload_form_dict = ezsignbulksenddocumentmapping_get_object_v2_response_m_payload.from_dict(ezsignbulksenddocumentmapping_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


