# WebhookSendWebhookV1Request

Request for POST /1/object/webhook/sendWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_webhook_module** | [**FieldEWebhookModule**](FieldEWebhookModule.md) |  | 
**e_webhook_ezsignevent** | [**CustomEWebhookEzsignevent**](CustomEWebhookEzsignevent.md) |  | [optional] 
**e_webhook_managementevent** | [**FieldEWebhookManagementevent**](FieldEWebhookManagementevent.md) |  | [optional] 
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | [optional] 
**fki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | [optional] 
**fki_ezsignsigner_id** | **int** | The unique ID of the Ezsignsigner | [optional] 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_userstaged_id** | **int** | The unique ID of the Userstaged | [optional] 

## Example

```python
from eZmaxApi.models.webhook_send_webhook_v1_request import WebhookSendWebhookV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSendWebhookV1Request from a JSON string
webhook_send_webhook_v1_request_instance = WebhookSendWebhookV1Request.from_json(json)
# print the JSON string representation of the object
print(WebhookSendWebhookV1Request.to_json())

# convert the object into a dict
webhook_send_webhook_v1_request_dict = webhook_send_webhook_v1_request_instance.to_dict()
# create an instance of WebhookSendWebhookV1Request from a dict
webhook_send_webhook_v1_request_from_dict = WebhookSendWebhookV1Request.from_dict(webhook_send_webhook_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


