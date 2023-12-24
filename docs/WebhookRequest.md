# WebhookRequest

A Webhook Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_webhook_id** | **int** | The unique ID of the Webhook | [optional] 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | [optional] 
**s_webhook_description** | **str** | The description of the Webhook | 
**e_webhook_module** | [**FieldEWebhookModule**](FieldEWebhookModule.md) |  | 
**e_webhook_ezsignevent** | [**FieldEWebhookEzsignevent**](FieldEWebhookEzsignevent.md) |  | [optional] 
**e_webhook_managementevent** | [**FieldEWebhookManagementevent**](FieldEWebhookManagementevent.md) |  | [optional] 
**s_webhook_url** | **str** | The URL of the Webhook callback | 
**s_webhook_emailfailed** | **str** | The email that will receive the Webhook in case all attempts fail | 
**b_webhook_isactive** | **bool** | Whether the Webhook is active or not | 
**b_webhook_issigned** | **bool** | Whether the requests will be signed or not | [optional] 
**b_webhook_skipsslvalidation** | **bool** | Wheter the server&#39;s SSL certificate should be validated or not. Not recommended to skip for production use | 

## Example

```python
from eZmaxApi.models.webhook_request import WebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRequest from a JSON string
webhook_request_instance = WebhookRequest.from_json(json)
# print the JSON string representation of the object
print WebhookRequest.to_json()

# convert the object into a dict
webhook_request_dict = webhook_request_instance.to_dict()
# create an instance of WebhookRequest from a dict
webhook_request_form_dict = webhook_request.from_dict(webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


