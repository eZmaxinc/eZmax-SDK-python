# CustomWebhookResponse

A custom Webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pks_customer_code** | **str** | The customer code assigned to your account | 
**b_webhook_test** | **bool** | Wheter the webhook received is a manual test or a real event | 
**e_webhook_emittype** | **str** | Wheter the webhook received is a manual test or a real event | [optional] 

## Example

```python
from eZmaxApi.models.custom_webhook_response import CustomWebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomWebhookResponse from a JSON string
custom_webhook_response_instance = CustomWebhookResponse.from_json(json)
# print the JSON string representation of the object
print(CustomWebhookResponse.to_json())

# convert the object into a dict
custom_webhook_response_dict = custom_webhook_response_instance.to_dict()
# create an instance of CustomWebhookResponse from a dict
custom_webhook_response_from_dict = CustomWebhookResponse.from_dict(custom_webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


