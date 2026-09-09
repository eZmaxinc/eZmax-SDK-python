# ElectronicfundstransferGetAttachmentsV1ResponseMPayload

Response for GET /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachmentdocumenttype** | [**List[CustomAttachmentdocumenttypeResponse]**](CustomAttachmentdocumenttypeResponse.md) |  | 

## Example

```python
from eZmaxApi.models.electronicfundstransfer_get_attachments_v1_response_m_payload import ElectronicfundstransferGetAttachmentsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicfundstransferGetAttachmentsV1ResponseMPayload from a JSON string
electronicfundstransfer_get_attachments_v1_response_m_payload_instance = ElectronicfundstransferGetAttachmentsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ElectronicfundstransferGetAttachmentsV1ResponseMPayload.to_json())

# convert the object into a dict
electronicfundstransfer_get_attachments_v1_response_m_payload_dict = electronicfundstransfer_get_attachments_v1_response_m_payload_instance.to_dict()
# create an instance of ElectronicfundstransferGetAttachmentsV1ResponseMPayload from a dict
electronicfundstransfer_get_attachments_v1_response_m_payload_from_dict = ElectronicfundstransferGetAttachmentsV1ResponseMPayload.from_dict(electronicfundstransfer_get_attachments_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


