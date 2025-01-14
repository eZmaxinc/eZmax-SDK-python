# WebhookRegenerateApikeyV1ResponseMPayload

Response for POST /1/object/webhook/{pkiWebhookID}/regenerateApikey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_webhook** | [**WebhookResponseCompound**](WebhookResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_regenerate_apikey_v1_response_m_payload import WebhookRegenerateApikeyV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRegenerateApikeyV1ResponseMPayload from a JSON string
webhook_regenerate_apikey_v1_response_m_payload_instance = WebhookRegenerateApikeyV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(WebhookRegenerateApikeyV1ResponseMPayload.to_json())

# convert the object into a dict
webhook_regenerate_apikey_v1_response_m_payload_dict = webhook_regenerate_apikey_v1_response_m_payload_instance.to_dict()
# create an instance of WebhookRegenerateApikeyV1ResponseMPayload from a dict
webhook_regenerate_apikey_v1_response_m_payload_from_dict = WebhookRegenerateApikeyV1ResponseMPayload.from_dict(webhook_regenerate_apikey_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


