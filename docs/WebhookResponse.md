# WebhookResponse

A webhook object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_webhook_id** | **int** | The Webhook ID. This value is visible in the admin interface. | 
**e_webhook_module** | **str** | The Module generating the Event. | 
**pks_customer_code** | **str** | The Customer Code in which the event was generated | 
**s_webhook_url** | **str** | The url being called | 
**s_webhook_emailfailed** | **str** | The email that will receive the webhook in case all attempts fail. | 
**e_webhook_ezsignevent** | **str** | This Ezsign Event. This property will be set only if the Module is \&quot;Ezsign\&quot;. | [optional] 
**e_webhook_managementevent** | **str** | This Management Event. This property will be set only if the Module is \&quot;Management\&quot;. | [optional]  if omitted the server will use the default value of "UserCreated"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


