# DiscussionGetObjectV2ResponseMPayload

Payload for GET /2/object/discussion/{pkiDiscussionID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_discussion** | [**DiscussionResponseCompound**](DiscussionResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.discussion_get_object_v2_response_m_payload import DiscussionGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionGetObjectV2ResponseMPayload from a JSON string
discussion_get_object_v2_response_m_payload_instance = DiscussionGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print DiscussionGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
discussion_get_object_v2_response_m_payload_dict = discussion_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of DiscussionGetObjectV2ResponseMPayload from a dict
discussion_get_object_v2_response_m_payload_form_dict = discussion_get_object_v2_response_m_payload.from_dict(discussion_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


