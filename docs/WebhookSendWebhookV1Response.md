# WebhookSendWebhookV1Response

Response for POST /1/object/webhook/sendWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from eZmaxApi.models.webhook_send_webhook_v1_response import WebhookSendWebhookV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSendWebhookV1Response from a JSON string
webhook_send_webhook_v1_response_instance = WebhookSendWebhookV1Response.from_json(json)
# print the JSON string representation of the object
print(WebhookSendWebhookV1Response.to_json())

# convert the object into a dict
webhook_send_webhook_v1_response_dict = webhook_send_webhook_v1_response_instance.to_dict()
# create an instance of WebhookSendWebhookV1Response from a dict
webhook_send_webhook_v1_response_from_dict = WebhookSendWebhookV1Response.from_dict(webhook_send_webhook_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


