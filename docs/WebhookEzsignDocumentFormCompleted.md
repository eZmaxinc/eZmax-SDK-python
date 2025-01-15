# WebhookEzsignDocumentFormCompleted

This is the base Webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_webhook** | [**CustomWebhookResponse**](CustomWebhookResponse.md) |  | 
**a_obj_attempt** | [**List[AttemptResponseCompound]**](AttemptResponse.md) | An array containing details of previous attempts that were made to deliver the message. The array is empty if it&#39;s the first attempt. | 
**obj_ezsigndocument** | [**EzsigndocumentResponse**](EzsigndocumentResponse.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_ezsign_document_form_completed import WebhookEzsignDocumentFormCompleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEzsignDocumentFormCompleted from a JSON string
webhook_ezsign_document_form_completed_instance = WebhookEzsignDocumentFormCompleted.from_json(json)
# print the JSON string representation of the object
print(WebhookEzsignDocumentFormCompleted.to_json())

# convert the object into a dict
webhook_ezsign_document_form_completed_dict = webhook_ezsign_document_form_completed_instance.to_dict()
# create an instance of WebhookEzsignDocumentFormCompleted from a dict
webhook_ezsign_document_form_completed_from_dict = WebhookEzsignDocumentFormCompleted.from_dict(webhook_ezsign_document_form_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


