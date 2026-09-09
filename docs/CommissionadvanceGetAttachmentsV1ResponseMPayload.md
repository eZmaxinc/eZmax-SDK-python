# CommissionadvanceGetAttachmentsV1ResponseMPayload

Response for GET /1/object/commissionadvance/{pkiCommissionadvanceID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachmentdocumenttype** | [**List[CustomAttachmentdocumenttypeResponse]**](CustomAttachmentdocumenttypeResponse.md) |  | 

## Example

```python
from eZmaxApi.models.commissionadvance_get_attachments_v1_response_m_payload import CommissionadvanceGetAttachmentsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionadvanceGetAttachmentsV1ResponseMPayload from a JSON string
commissionadvance_get_attachments_v1_response_m_payload_instance = CommissionadvanceGetAttachmentsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CommissionadvanceGetAttachmentsV1ResponseMPayload.to_json())

# convert the object into a dict
commissionadvance_get_attachments_v1_response_m_payload_dict = commissionadvance_get_attachments_v1_response_m_payload_instance.to_dict()
# create an instance of CommissionadvanceGetAttachmentsV1ResponseMPayload from a dict
commissionadvance_get_attachments_v1_response_m_payload_from_dict = CommissionadvanceGetAttachmentsV1ResponseMPayload.from_dict(commissionadvance_get_attachments_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


