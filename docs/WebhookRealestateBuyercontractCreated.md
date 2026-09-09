# WebhookRealestateBuyercontractCreated

This is the base Webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_webhook** | [**CustomWebhookResponse**](CustomWebhookResponse.md) |  | 
**a_obj_attempt** | [**List[AttemptResponseCompound]**](AttemptResponseCompound.md) | An array containing details of previous attempts that were made to deliver the message. The array is empty if it&#39;s the first attempt. | 
**obj_buyercontract** | [**BuyercontractResponse**](BuyercontractResponse.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_realestate_buyercontract_created import WebhookRealestateBuyercontractCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRealestateBuyercontractCreated from a JSON string
webhook_realestate_buyercontract_created_instance = WebhookRealestateBuyercontractCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookRealestateBuyercontractCreated.to_json())

# convert the object into a dict
webhook_realestate_buyercontract_created_dict = webhook_realestate_buyercontract_created_instance.to_dict()
# create an instance of WebhookRealestateBuyercontractCreated from a dict
webhook_realestate_buyercontract_created_from_dict = WebhookRealestateBuyercontractCreated.from_dict(webhook_realestate_buyercontract_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


