# WebhookCreateObjectV2ResponseMPayload

Payload for POST /2/object/webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_webhook** | [**List[WebhookResponseCompound]**](WebhookResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_create_object_v2_response_m_payload import WebhookCreateObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCreateObjectV2ResponseMPayload from a JSON string
webhook_create_object_v2_response_m_payload_instance = WebhookCreateObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print WebhookCreateObjectV2ResponseMPayload.to_json()

# convert the object into a dict
webhook_create_object_v2_response_m_payload_dict = webhook_create_object_v2_response_m_payload_instance.to_dict()
# create an instance of WebhookCreateObjectV2ResponseMPayload from a dict
webhook_create_object_v2_response_m_payload_form_dict = webhook_create_object_v2_response_m_payload.from_dict(webhook_create_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


