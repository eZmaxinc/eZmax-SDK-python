# WebhookGetObjectV2ResponseMPayload

Payload for GET /2/object/webhook/{pkiWebhookID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_webhook** | [**WebhookResponseCompound**](WebhookResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_get_object_v2_response_m_payload import WebhookGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookGetObjectV2ResponseMPayload from a JSON string
webhook_get_object_v2_response_m_payload_instance = WebhookGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(WebhookGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
webhook_get_object_v2_response_m_payload_dict = webhook_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of WebhookGetObjectV2ResponseMPayload from a dict
webhook_get_object_v2_response_m_payload_from_dict = WebhookGetObjectV2ResponseMPayload.from_dict(webhook_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


