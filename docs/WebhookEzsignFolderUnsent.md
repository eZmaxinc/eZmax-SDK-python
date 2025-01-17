# WebhookEzsignFolderUnsent

This is the base Webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfolder** | [**EzsignfolderResponse**](EzsignfolderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_ezsign_folder_unsent import WebhookEzsignFolderUnsent

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEzsignFolderUnsent from a JSON string
webhook_ezsign_folder_unsent_instance = WebhookEzsignFolderUnsent.from_json(json)
# print the JSON string representation of the object
print(WebhookEzsignFolderUnsent.to_json())

# convert the object into a dict
webhook_ezsign_folder_unsent_dict = webhook_ezsign_folder_unsent_instance.to_dict()
# create an instance of WebhookEzsignFolderUnsent from a dict
webhook_ezsign_folder_unsent_from_dict = WebhookEzsignFolderUnsent.from_dict(webhook_ezsign_folder_unsent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


