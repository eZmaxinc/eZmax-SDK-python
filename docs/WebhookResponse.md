# WebhookResponse

A webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_webhook_id** | **int** | The unique ID of the Webhook | 
**s_webhook_description** | **str** | The description of the Webhook | 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | [optional] 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | [optional] 
**e_webhook_module** | [**FieldEWebhookModule**](FieldEWebhookModule.md) |  | 
**e_webhook_ezsignevent** | [**FieldEWebhookEzsignevent**](FieldEWebhookEzsignevent.md) |  | [optional] 
**e_webhook_managementevent** | [**FieldEWebhookManagementevent**](FieldEWebhookManagementevent.md) |  | [optional] 
**s_webhook_url** | **str** | The URL of the Webhook callback | 
**s_webhook_emailfailed** | **str** | The email that will receive the Webhook in case all attempts fail | 
**s_webhook_apikey** | **str** | The Apikey for the Webhook.  This will be hidden if we are not creating or regenerating the Apikey. | [optional] 
**s_webhook_secret** | **str** | The Secret for the Webhook.  This will be hidden if we are not creating or regenerating the Apikey. | [optional] 
**b_webhook_isactive** | **bool** | Whether the Webhook is active or not | 
**b_webhook_issigned** | **bool** | Whether the requests will be signed or not | 
**b_webhook_skipsslvalidation** | **bool** | Wheter the server&#39;s SSL certificate should be validated or not. Not recommended to skip for production use | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_response import WebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookResponse from a JSON string
webhook_response_instance = WebhookResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookResponse.to_json())

# convert the object into a dict
webhook_response_dict = webhook_response_instance.to_dict()
# create an instance of WebhookResponse from a dict
webhook_response_form_dict = webhook_response.from_dict(webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


