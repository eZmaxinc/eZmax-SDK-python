# WebhookRealestateInscriptionnotauthenticatedModified

This is a webhook for a RealestateInscriptionnotauthenticatedModified event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_webhook** | [**CustomWebhookResponse**](CustomWebhookResponse.md) |  | 
**a_obj_attempt** | [**List[AttemptResponseCompound]**](AttemptResponseCompound.md) | An array containing details of previous attempts that were made to deliver the message. The array is empty if it&#39;s the first attempt. | 
**obj_inscriptionnotauthenticated** | [**InscriptionnotauthenticatedResponse**](InscriptionnotauthenticatedResponse.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_realestate_inscriptionnotauthenticated_modified import WebhookRealestateInscriptionnotauthenticatedModified

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRealestateInscriptionnotauthenticatedModified from a JSON string
webhook_realestate_inscriptionnotauthenticated_modified_instance = WebhookRealestateInscriptionnotauthenticatedModified.from_json(json)
# print the JSON string representation of the object
print(WebhookRealestateInscriptionnotauthenticatedModified.to_json())

# convert the object into a dict
webhook_realestate_inscriptionnotauthenticated_modified_dict = webhook_realestate_inscriptionnotauthenticated_modified_instance.to_dict()
# create an instance of WebhookRealestateInscriptionnotauthenticatedModified from a dict
webhook_realestate_inscriptionnotauthenticated_modified_from_dict = WebhookRealestateInscriptionnotauthenticatedModified.from_dict(webhook_realestate_inscriptionnotauthenticated_modified_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


