# WebhookEzsignFolderCompleted

This is the base Webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_webhook** | [**CustomWebhookResponse**](CustomWebhookResponse.md) |  | 
**a_obj_attempt** | [**List[AttemptResponseCompound]**](AttemptResponseCompound.md) | An array containing details of previous attempts that were made to deliver the message. The array is empty if it&#39;s the first attempt. | 
**obj_ezsignfolder** | [**EzsignfolderResponse**](EzsignfolderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_ezsign_folder_completed import WebhookEzsignFolderCompleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEzsignFolderCompleted from a JSON string
webhook_ezsign_folder_completed_instance = WebhookEzsignFolderCompleted.from_json(json)
# print the JSON string representation of the object
print(WebhookEzsignFolderCompleted.to_json())

# convert the object into a dict
webhook_ezsign_folder_completed_dict = webhook_ezsign_folder_completed_instance.to_dict()
# create an instance of WebhookEzsignFolderCompleted from a dict
webhook_ezsign_folder_completed_form_dict = webhook_ezsign_folder_completed.from_dict(webhook_ezsign_folder_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


