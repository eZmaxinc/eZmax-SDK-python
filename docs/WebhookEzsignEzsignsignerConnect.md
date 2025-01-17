# WebhookEzsignEzsignsignerConnect

This is the base Webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfolder** | [**EzsignfolderResponse**](EzsignfolderResponse.md) |  | [optional] 
**obj_ezsignfoldersignerassociation** | [**EzsignfoldersignerassociationResponseCompound**](EzsignfoldersignerassociationResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_ezsign_ezsignsigner_connect import WebhookEzsignEzsignsignerConnect

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEzsignEzsignsignerConnect from a JSON string
webhook_ezsign_ezsignsigner_connect_instance = WebhookEzsignEzsignsignerConnect.from_json(json)
# print the JSON string representation of the object
print(WebhookEzsignEzsignsignerConnect.to_json())

# convert the object into a dict
webhook_ezsign_ezsignsigner_connect_dict = webhook_ezsign_ezsignsigner_connect_instance.to_dict()
# create an instance of WebhookEzsignEzsignsignerConnect from a dict
webhook_ezsign_ezsignsigner_connect_from_dict = WebhookEzsignEzsignsignerConnect.from_dict(webhook_ezsign_ezsignsigner_connect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


