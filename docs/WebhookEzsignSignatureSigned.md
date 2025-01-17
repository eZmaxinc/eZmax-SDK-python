# WebhookEzsignSignatureSigned

This is the base Webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignsignature** | [**EzsignsignatureResponse**](EzsignsignatureResponse.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_ezsign_signature_signed import WebhookEzsignSignatureSigned

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEzsignSignatureSigned from a JSON string
webhook_ezsign_signature_signed_instance = WebhookEzsignSignatureSigned.from_json(json)
# print the JSON string representation of the object
print(WebhookEzsignSignatureSigned.to_json())

# convert the object into a dict
webhook_ezsign_signature_signed_dict = webhook_ezsign_signature_signed_instance.to_dict()
# create an instance of WebhookEzsignSignatureSigned from a dict
webhook_ezsign_signature_signed_from_dict = WebhookEzsignSignatureSigned.from_dict(webhook_ezsign_signature_signed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


