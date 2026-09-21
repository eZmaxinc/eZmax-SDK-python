# AttachmentDocumentTypeV1Request

Request for POST /1/object/attachment/{pkiAttachmentID}/documentType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_documenttypechecklist_id** | **int** | The unique ID of the Documenttypechecklist or null | 

## Example

```python
from eZmaxApi.models.attachment_document_type_v1_request import AttachmentDocumentTypeV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentDocumentTypeV1Request from a JSON string
attachment_document_type_v1_request_instance = AttachmentDocumentTypeV1Request.from_json(json)
# print the JSON string representation of the object
print(AttachmentDocumentTypeV1Request.to_json())

# convert the object into a dict
attachment_document_type_v1_request_dict = attachment_document_type_v1_request_instance.to_dict()
# create an instance of AttachmentDocumentTypeV1Request from a dict
attachment_document_type_v1_request_from_dict = AttachmentDocumentTypeV1Request.from_dict(attachment_document_type_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


