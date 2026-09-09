# LeadGetAttachmentsV1ResponseMPayload

Response for GET /1/object/lead/{pkiLeadID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachmentdocumenttype** | [**List[CustomAttachmentdocumenttypeResponse]**](CustomAttachmentdocumenttypeResponse.md) |  | 

## Example

```python
from eZmaxApi.models.lead_get_attachments_v1_response_m_payload import LeadGetAttachmentsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of LeadGetAttachmentsV1ResponseMPayload from a JSON string
lead_get_attachments_v1_response_m_payload_instance = LeadGetAttachmentsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(LeadGetAttachmentsV1ResponseMPayload.to_json())

# convert the object into a dict
lead_get_attachments_v1_response_m_payload_dict = lead_get_attachments_v1_response_m_payload_instance.to_dict()
# create an instance of LeadGetAttachmentsV1ResponseMPayload from a dict
lead_get_attachments_v1_response_m_payload_from_dict = LeadGetAttachmentsV1ResponseMPayload.from_dict(lead_get_attachments_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


