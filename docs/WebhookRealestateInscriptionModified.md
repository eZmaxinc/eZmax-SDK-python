# WebhookRealestateInscriptionModified

This is a webhook for a RealestateInscriptionModified event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_webhook** | [**CustomWebhookResponse**](CustomWebhookResponse.md) |  | 
**a_obj_attempt** | [**List[AttemptResponseCompound]**](AttemptResponseCompound.md) | An array containing details of previous attempts that were made to deliver the message. The array is empty if it&#39;s the first attempt. | 
**obj_inscription** | [**InscriptionResponse**](InscriptionResponse.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_realestate_inscription_modified import WebhookRealestateInscriptionModified

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRealestateInscriptionModified from a JSON string
webhook_realestate_inscription_modified_instance = WebhookRealestateInscriptionModified.from_json(json)
# print the JSON string representation of the object
print(WebhookRealestateInscriptionModified.to_json())

# convert the object into a dict
webhook_realestate_inscription_modified_dict = webhook_realestate_inscription_modified_instance.to_dict()
# create an instance of WebhookRealestateInscriptionModified from a dict
webhook_realestate_inscription_modified_from_dict = WebhookRealestateInscriptionModified.from_dict(webhook_realestate_inscription_modified_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


