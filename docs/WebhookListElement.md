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
**b_webhook_isactive** | **bool** | Whether the Webhook is active or not | 
**e_webhook_ezsignevent** | [**FieldEWebhookEzsignevent**](FieldEWebhookEzsignevent.md) |  | [optional] 
**e_webhook_managementevent** | [**FieldEWebhookManagementevent**](FieldEWebhookManagementevent.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


