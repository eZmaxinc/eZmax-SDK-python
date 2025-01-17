# WebhookEzsignFolderCompleted

This is the base Webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
webhook_ezsign_folder_completed_from_dict = WebhookEzsignFolderCompleted.from_dict(webhook_ezsign_folder_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


