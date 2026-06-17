# WebhookEzmaxpartnerproductUnsubscribe

This is the base Webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_webhook** | [**CustomWebhookResponse**](CustomWebhookResponse.md) |  | 
**a_obj_attempt** | [**List[AttemptResponseCompound]**](AttemptResponseCompound.md) | An array containing details of previous attempts that were made to deliver the message. The array is empty if it&#39;s the first attempt. | 
**obj_ezmaxpartnerproduct** | [**CustomEzmaxpartnerproductSubscribe**](CustomEzmaxpartnerproductSubscribe.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_ezmaxpartnerproduct_unsubscribe import WebhookEzmaxpartnerproductUnsubscribe

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEzmaxpartnerproductUnsubscribe from a JSON string
webhook_ezmaxpartnerproduct_unsubscribe_instance = WebhookEzmaxpartnerproductUnsubscribe.from_json(json)
# print the JSON string representation of the object
print(WebhookEzmaxpartnerproductUnsubscribe.to_json())

# convert the object into a dict
webhook_ezmaxpartnerproduct_unsubscribe_dict = webhook_ezmaxpartnerproduct_unsubscribe_instance.to_dict()
# create an instance of WebhookEzmaxpartnerproductUnsubscribe from a dict
webhook_ezmaxpartnerproduct_unsubscribe_from_dict = WebhookEzmaxpartnerproductUnsubscribe.from_dict(webhook_ezmaxpartnerproduct_unsubscribe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


