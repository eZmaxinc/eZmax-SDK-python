# EzsignuserGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsignuser/{pkiEzsignuserID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignuser** | [**EzsignuserResponseCompound**](EzsignuserResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignuser_get_object_v2_response_m_payload import EzsignuserGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignuserGetObjectV2ResponseMPayload from a JSON string
ezsignuser_get_object_v2_response_m_payload_instance = EzsignuserGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignuserGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsignuser_get_object_v2_response_m_payload_dict = ezsignuser_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignuserGetObjectV2ResponseMPayload from a dict
ezsignuser_get_object_v2_response_m_payload_from_dict = EzsignuserGetObjectV2ResponseMPayload.from_dict(ezsignuser_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


