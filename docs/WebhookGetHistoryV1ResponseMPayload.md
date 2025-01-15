# WebhookGetHistoryV1ResponseMPayload

Payload for GET /1/object/webhook/{pkiWebhookID}/getHistory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_webhooklog** | **List[CustomWebhooklogResponse]** |  | 

## Example

```python
from eZmaxApi.models.webhook_get_history_v1_response_m_payload import WebhookGetHistoryV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookGetHistoryV1ResponseMPayload from a JSON string
webhook_get_history_v1_response_m_payload_instance = WebhookGetHistoryV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(WebhookGetHistoryV1ResponseMPayload.to_json())

# convert the object into a dict
webhook_get_history_v1_response_m_payload_dict = webhook_get_history_v1_response_m_payload_instance.to_dict()
# create an instance of WebhookGetHistoryV1ResponseMPayload from a dict
webhook_get_history_v1_response_m_payload_from_dict = WebhookGetHistoryV1ResponseMPayload.from_dict(webhook_get_history_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


