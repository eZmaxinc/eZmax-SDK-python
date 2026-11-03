# AttachmentSetDocumentTypeV1Request

Request for POST /1/object/attachment/{pkiAttachmentID}/setDocumentType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_documenttypechecklist_id** | **int** | The unique ID of the Documenttypechecklist or null | 

## Example

```python
from eZmaxApi.models.attachment_set_document_type_v1_request import AttachmentSetDocumentTypeV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentSetDocumentTypeV1Request from a JSON string
attachment_set_document_type_v1_request_instance = AttachmentSetDocumentTypeV1Request.from_json(json)
# print the JSON string representation of the object
print(AttachmentSetDocumentTypeV1Request.to_json())

# convert the object into a dict
attachment_set_document_type_v1_request_dict = attachment_set_document_type_v1_request_instance.to_dict()
# create an instance of AttachmentSetDocumentTypeV1Request from a dict
attachment_set_document_type_v1_request_from_dict = AttachmentSetDocumentTypeV1Request.from_dict(attachment_set_document_type_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


