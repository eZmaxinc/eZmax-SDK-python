# WebhookEzsignFolderSent

This is the base Webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_webhook** | [**CustomWebhookResponse**](CustomWebhookResponse.md) |  | 
**a_obj_attempt** | [**List[AttemptResponseCompound]**](AttemptResponseCompound.md) | An array containing details of previous attempts that were made to deliver the message. The array is empty if it&#39;s the first attempt. | 
**obj_ezsignfolder** | [**EzsignfolderResponse**](EzsignfolderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_ezsign_folder_sent import WebhookEzsignFolderSent

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEzsignFolderSent from a JSON string
webhook_ezsign_folder_sent_instance = WebhookEzsignFolderSent.from_json(json)
# print the JSON string representation of the object
print(WebhookEzsignFolderSent.to_json())

# convert the object into a dict
webhook_ezsign_folder_sent_dict = webhook_ezsign_folder_sent_instance.to_dict()
# create an instance of WebhookEzsignFolderSent from a dict
webhook_ezsign_folder_sent_form_dict = webhook_ezsign_folder_sent.from_dict(webhook_ezsign_folder_sent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


