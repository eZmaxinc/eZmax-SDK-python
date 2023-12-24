# WebhookGetHistoryV1Response

Response for GET /1/object/webhook/{pkiWebhookID}/getHistory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**WebhookGetHistoryV1ResponseMPayload**](WebhookGetHistoryV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_get_history_v1_response import WebhookGetHistoryV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookGetHistoryV1Response from a JSON string
webhook_get_history_v1_response_instance = WebhookGetHistoryV1Response.from_json(json)
# print the JSON string representation of the object
print WebhookGetHistoryV1Response.to_json()

# convert the object into a dict
webhook_get_history_v1_response_dict = webhook_get_history_v1_response_instance.to_dict()
# create an instance of WebhookGetHistoryV1Response from a dict
webhook_get_history_v1_response_form_dict = webhook_get_history_v1_response.from_dict(webhook_get_history_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


