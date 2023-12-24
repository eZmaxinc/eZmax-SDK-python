# WebhookRegenerateApikeyV1Response

Response for POST /1/object/webhook/{pkiWebhookID}/regenerateApikey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**WebhookRegenerateApikeyV1ResponseMPayload**](WebhookRegenerateApikeyV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_regenerate_apikey_v1_response import WebhookRegenerateApikeyV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRegenerateApikeyV1Response from a JSON string
webhook_regenerate_apikey_v1_response_instance = WebhookRegenerateApikeyV1Response.from_json(json)
# print the JSON string representation of the object
print WebhookRegenerateApikeyV1Response.to_json()

# convert the object into a dict
webhook_regenerate_apikey_v1_response_dict = webhook_regenerate_apikey_v1_response_instance.to_dict()
# create an instance of WebhookRegenerateApikeyV1Response from a dict
webhook_regenerate_apikey_v1_response_form_dict = webhook_regenerate_apikey_v1_response.from_dict(webhook_regenerate_apikey_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


