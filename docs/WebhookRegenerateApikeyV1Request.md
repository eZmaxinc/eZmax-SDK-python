# WebhookRegenerateApikeyV1Request

Request for POST /1/object/webhook/{pkiWebhookID}/regenerateApikey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_webhook_issigned** | **bool** | Whether the requests will be signed or not | [optional] 

## Example

```python
from eZmaxApi.models.webhook_regenerate_apikey_v1_request import WebhookRegenerateApikeyV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRegenerateApikeyV1Request from a JSON string
webhook_regenerate_apikey_v1_request_instance = WebhookRegenerateApikeyV1Request.from_json(json)
# print the JSON string representation of the object
print(WebhookRegenerateApikeyV1Request.to_json())

# convert the object into a dict
webhook_regenerate_apikey_v1_request_dict = webhook_regenerate_apikey_v1_request_instance.to_dict()
# create an instance of WebhookRegenerateApikeyV1Request from a dict
webhook_regenerate_apikey_v1_request_from_dict = WebhookRegenerateApikeyV1Request.from_dict(webhook_regenerate_apikey_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


