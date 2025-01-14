# CustomAttachmentdocumenttypeResponse

An Attachmentdocumenttype

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_attachment_documenttype** | [**FieldEAttachmentDocumenttype**](FieldEAttachmentDocumenttype.md) |  | 
**a_obj_attachment** | [**List[CustomAttachmentResponse]**](CustomAttachmentResponse.md) |  | 

## Example

```python
from eZmaxApi.models.custom_attachmentdocumenttype_response import CustomAttachmentdocumenttypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttachmentdocumenttypeResponse from a JSON string
custom_attachmentdocumenttype_response_instance = CustomAttachmentdocumenttypeResponse.from_json(json)
# print the JSON string representation of the object
print(CustomAttachmentdocumenttypeResponse.to_json())

# convert the object into a dict
custom_attachmentdocumenttype_response_dict = custom_attachmentdocumenttype_response_instance.to_dict()
# create an instance of CustomAttachmentdocumenttypeResponse from a dict
custom_attachmentdocumenttype_response_from_dict = CustomAttachmentdocumenttypeResponse.from_dict(custom_attachmentdocumenttype_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


