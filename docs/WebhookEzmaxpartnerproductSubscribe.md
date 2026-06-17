# WebhookEzmaxpartnerproductSubscribe

This is the base Webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_webhook** | [**CustomWebhookResponse**](CustomWebhookResponse.md) |  | 
**a_obj_attempt** | [**List[AttemptResponseCompound]**](AttemptResponseCompound.md) | An array containing details of previous attempts that were made to deliver the message. The array is empty if it&#39;s the first attempt. | 
**obj_ezmaxpartnerproduct** | [**CustomEzmaxpartnerproductSubscribe**](CustomEzmaxpartnerproductSubscribe.md) |  | 
**s_external_id** | **str** |  | [optional] 
**s_apikey_apikey** | **str** |  | [optional] 
**s_apikey_secret** | **str** |  | [optional] 

## Example

```python
from eZmaxApi.models.webhook_ezmaxpartnerproduct_subscribe import WebhookEzmaxpartnerproductSubscribe

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEzmaxpartnerproductSubscribe from a JSON string
webhook_ezmaxpartnerproduct_subscribe_instance = WebhookEzmaxpartnerproductSubscribe.from_json(json)
# print the JSON string representation of the object
print(WebhookEzmaxpartnerproductSubscribe.to_json())

# convert the object into a dict
webhook_ezmaxpartnerproduct_subscribe_dict = webhook_ezmaxpartnerproduct_subscribe_instance.to_dict()
# create an instance of WebhookEzmaxpartnerproductSubscribe from a dict
webhook_ezmaxpartnerproduct_subscribe_from_dict = WebhookEzmaxpartnerproductSubscribe.from_dict(webhook_ezmaxpartnerproduct_subscribe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


