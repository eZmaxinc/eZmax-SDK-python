# EzsignannotationGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsignannotation/{pkiEzsignannotationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignannotation** | [**EzsignannotationResponseCompound**](EzsignannotationResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignannotation_get_object_v2_response_m_payload import EzsignannotationGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignannotationGetObjectV2ResponseMPayload from a JSON string
ezsignannotation_get_object_v2_response_m_payload_instance = EzsignannotationGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignannotationGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsignannotation_get_object_v2_response_m_payload_dict = ezsignannotation_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignannotationGetObjectV2ResponseMPayload from a dict
ezsignannotation_get_object_v2_response_m_payload_from_dict = EzsignannotationGetObjectV2ResponseMPayload.from_dict(ezsignannotation_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


