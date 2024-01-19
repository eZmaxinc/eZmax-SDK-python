# EzsigndiscussionGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsigndiscussion/{pkiEzsigndiscussionID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigndiscussion** | [**EzsigndiscussionResponseCompound**](EzsigndiscussionResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndiscussion_get_object_v2_response_m_payload import EzsigndiscussionGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndiscussionGetObjectV2ResponseMPayload from a JSON string
ezsigndiscussion_get_object_v2_response_m_payload_instance = EzsigndiscussionGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsigndiscussionGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
ezsigndiscussion_get_object_v2_response_m_payload_dict = ezsigndiscussion_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigndiscussionGetObjectV2ResponseMPayload from a dict
ezsigndiscussion_get_object_v2_response_m_payload_form_dict = ezsigndiscussion_get_object_v2_response_m_payload.from_dict(ezsigndiscussion_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


