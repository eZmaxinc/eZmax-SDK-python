# WebhookEzsignDocumentCompleted

This is the base Webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigndocument** | [**EzsigndocumentResponse**](EzsigndocumentResponse.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_ezsign_document_completed import WebhookEzsignDocumentCompleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEzsignDocumentCompleted from a JSON string
webhook_ezsign_document_completed_instance = WebhookEzsignDocumentCompleted.from_json(json)
# print the JSON string representation of the object
print(WebhookEzsignDocumentCompleted.to_json())

# convert the object into a dict
webhook_ezsign_document_completed_dict = webhook_ezsign_document_completed_instance.to_dict()
# create an instance of WebhookEzsignDocumentCompleted from a dict
webhook_ezsign_document_completed_from_dict = WebhookEzsignDocumentCompleted.from_dict(webhook_ezsign_document_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


