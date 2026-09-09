# WebhookRealestateBuyercontractModified

This is the base Webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_webhook** | [**CustomWebhookResponse**](CustomWebhookResponse.md) |  | 
**a_obj_attempt** | [**List[AttemptResponseCompound]**](AttemptResponseCompound.md) | An array containing details of previous attempts that were made to deliver the message. The array is empty if it&#39;s the first attempt. | 
**obj_buyercontract** | [**BuyercontractResponse**](BuyercontractResponse.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_realestate_buyercontract_modified import WebhookRealestateBuyercontractModified

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRealestateBuyercontractModified from a JSON string
webhook_realestate_buyercontract_modified_instance = WebhookRealestateBuyercontractModified.from_json(json)
# print the JSON string representation of the object
print(WebhookRealestateBuyercontractModified.to_json())

# convert the object into a dict
webhook_realestate_buyercontract_modified_dict = webhook_realestate_buyercontract_modified_instance.to_dict()
# create an instance of WebhookRealestateBuyercontractModified from a dict
webhook_realestate_buyercontract_modified_from_dict = WebhookRealestateBuyercontractModified.from_dict(webhook_realestate_buyercontract_modified_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


