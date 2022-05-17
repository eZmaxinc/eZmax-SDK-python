# WebhookResponse

A webhook object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pks_customer_code** | [**FieldPksCustomerCode**](FieldPksCustomerCode.md) |  | 
**pki_webhook_id** | **int** | The Webhook ID. This value is visible in the admin interface. | 
**e_webhook_module** | **str** | The Module generating the Event. | 
**s_webhook_url** | **str** | The url being called | 
**b_webhook_test** | **bool** | Wheter the webhook received is a manual test or a real event | 
**b_webhook_skipsslvalidation** | **bool** | Wheter the server&#39;s SSL certificate should be validated or not. Not recommended for production use. | 
**s_webhook_emailfailed** | **str** | The email that will receive the webhook in case all attempts fail. | 
**e_webhook_ezsignevent** | **str** | This Ezsign Event. This property will be set only if the Module is \&quot;Ezsign\&quot;. | [optional] 
**e_webhook_managementevent** | **str** | This Management Event. This property will be set only if the Module is \&quot;Management\&quot;. | [optional]  if omitted the server will use the default value of "UserCreated"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


