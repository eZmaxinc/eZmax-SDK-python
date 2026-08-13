# EzsignbulksenddocumentmappingGetObjectV3ResponseMPayload

Payload for GET /3/object/ezsignbulksenddocumentmapping/{pkiEzsignbulksenddocumentmappingID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignbulksenddocumentmapping** | [**EzsignbulksenddocumentmappingResponseCompoundV3**](EzsignbulksenddocumentmappingResponseCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksenddocumentmapping_get_object_v3_response_m_payload import EzsignbulksenddocumentmappingGetObjectV3ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksenddocumentmappingGetObjectV3ResponseMPayload from a JSON string
ezsignbulksenddocumentmapping_get_object_v3_response_m_payload_instance = EzsignbulksenddocumentmappingGetObjectV3ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksenddocumentmappingGetObjectV3ResponseMPayload.to_json())

# convert the object into a dict
ezsignbulksenddocumentmapping_get_object_v3_response_m_payload_dict = ezsignbulksenddocumentmapping_get_object_v3_response_m_payload_instance.to_dict()
# create an instance of EzsignbulksenddocumentmappingGetObjectV3ResponseMPayload from a dict
ezsignbulksenddocumentmapping_get_object_v3_response_m_payload_from_dict = EzsignbulksenddocumentmappingGetObjectV3ResponseMPayload.from_dict(ezsignbulksenddocumentmapping_get_object_v3_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


