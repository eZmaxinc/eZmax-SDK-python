# SystemconfigurationGetObjectV2ResponseMPayload

Payload for GET /2/object/systemconfiguration/{pkiSystemconfigurationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_systemconfiguration** | [**SystemconfigurationResponseCompound**](SystemconfigurationResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.systemconfiguration_get_object_v2_response_m_payload import SystemconfigurationGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SystemconfigurationGetObjectV2ResponseMPayload from a JSON string
systemconfiguration_get_object_v2_response_m_payload_instance = SystemconfigurationGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SystemconfigurationGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
systemconfiguration_get_object_v2_response_m_payload_dict = systemconfiguration_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of SystemconfigurationGetObjectV2ResponseMPayload from a dict
systemconfiguration_get_object_v2_response_m_payload_from_dict = SystemconfigurationGetObjectV2ResponseMPayload.from_dict(systemconfiguration_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


