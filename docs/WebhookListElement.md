# WebhookListElement

A Webhook List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_webhook_id** | **int** | The unique ID of the Webhook | 
**s_webhook_description** | **str** | The description of the Webhook | 
**s_webhook_url** | **str** | The URL of the Webhook callback | 
**s_webhook_event** | **str** | The concatenated string to describe the Webhook event | 
**s_webhook_emailfailed** | **str** | The email that will receive the Webhook in case all attempts fail | 
**e_webhook_module** | [**FieldEWebhookModule**](FieldEWebhookModule.md) |  | 
**e_webhook_ezsignevent** | [**FieldEWebhookEzsignevent**](FieldEWebhookEzsignevent.md) |  | [optional] 
**e_webhook_managementevent** | [**FieldEWebhookManagementevent**](FieldEWebhookManagementevent.md) |  | [optional] 
**b_webhook_isactive** | **bool** | Whether the Webhook is active or not | 
**b_webhook_issigned** | **bool** | Whether the requests will be signed or not | 

## Example

```python
from eZmaxApi.models.webhook_list_element import WebhookListElement

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookListElement from a JSON string
webhook_list_element_instance = WebhookListElement.from_json(json)
# print the JSON string representation of the object
print WebhookListElement.to_json()

# convert the object into a dict
webhook_list_element_dict = webhook_list_element_instance.to_dict()
# create an instance of WebhookListElement from a dict
webhook_list_element_form_dict = webhook_list_element.from_dict(webhook_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


