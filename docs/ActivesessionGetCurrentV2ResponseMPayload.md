# ActivesessionGetCurrentV2ResponseMPayload

Payload for GET /1/object/activesession/getCurrent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_activesession** | [**ActivesessionResponseCompound**](ActivesessionResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.activesession_get_current_v2_response_m_payload import ActivesessionGetCurrentV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ActivesessionGetCurrentV2ResponseMPayload from a JSON string
activesession_get_current_v2_response_m_payload_instance = ActivesessionGetCurrentV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ActivesessionGetCurrentV2ResponseMPayload.to_json())

# convert the object into a dict
activesession_get_current_v2_response_m_payload_dict = activesession_get_current_v2_response_m_payload_instance.to_dict()
# create an instance of ActivesessionGetCurrentV2ResponseMPayload from a dict
activesession_get_current_v2_response_m_payload_from_dict = ActivesessionGetCurrentV2ResponseMPayload.from_dict(activesession_get_current_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


