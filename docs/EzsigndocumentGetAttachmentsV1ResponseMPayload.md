# EzsigndocumentGetAttachmentsV1ResponseMPayload

Response for GET /1/object/ezsigndocument/{pkiEzsigndocumentID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachmentdocumenttype** | [**List[CustomAttachmentdocumenttypeResponse]**](CustomAttachmentdocumenttypeResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_attachments_v1_response_m_payload import EzsigndocumentGetAttachmentsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetAttachmentsV1ResponseMPayload from a JSON string
ezsigndocument_get_attachments_v1_response_m_payload_instance = EzsigndocumentGetAttachmentsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetAttachmentsV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigndocument_get_attachments_v1_response_m_payload_dict = ezsigndocument_get_attachments_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigndocumentGetAttachmentsV1ResponseMPayload from a dict
ezsigndocument_get_attachments_v1_response_m_payload_from_dict = EzsigndocumentGetAttachmentsV1ResponseMPayload.from_dict(ezsigndocument_get_attachments_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


