# WebhookResponseCompound

A Webhook Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_webhook_event** | **str** | The concatenated string to describe the Webhook event | 
**pki_webhook_id** | **int** | The unique ID of the Webhook | 
**s_webhook_description** | **str** | The description of the Webhook | 
**e_webhook_module** | [**FieldEWebhookModule**](FieldEWebhookModule.md) |  | 
**s_webhook_url** | **str** | The URL of the Webhook callback | 
**s_webhook_emailfailed** | **str** | The email that will receive the Webhook in case all attempts fail | 
**b_webhook_skipsslvalidation** | **bool** | Wheter the server&#39;s SSL certificate should be validated or not. Not recommended to skip for production use | 
**fki_ezsignfoldertype_id** | [**FieldPkiEzsignfoldertypeID**](FieldPkiEzsignfoldertypeID.md) |  | [optional] 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | [optional] 
**e_webhook_ezsignevent** | [**FieldEWebhookEzsignevent**](FieldEWebhookEzsignevent.md) |  | [optional] 
**e_webhook_managementevent** | [**FieldEWebhookManagementevent**](FieldEWebhookManagementevent.md) |  | [optional] 
**b_webhook_isactive** | **bool** | Whether the Webhook is active or not | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


