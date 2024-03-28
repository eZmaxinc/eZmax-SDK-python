# EzsignsigningreasonGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsignsigningreason/{pkiEzsignsigningreasonID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignsigningreason** | [**EzsignsigningreasonResponseCompound**](EzsignsigningreasonResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsigningreason_get_object_v2_response_m_payload import EzsignsigningreasonGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsigningreasonGetObjectV2ResponseMPayload from a JSON string
ezsignsigningreason_get_object_v2_response_m_payload_instance = EzsignsigningreasonGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignsigningreasonGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsignsigningreason_get_object_v2_response_m_payload_dict = ezsignsigningreason_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignsigningreasonGetObjectV2ResponseMPayload from a dict
ezsignsigningreason_get_object_v2_response_m_payload_form_dict = ezsignsigningreason_get_object_v2_response_m_payload.from_dict(ezsignsigningreason_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


