# ExternalbrokerGetAttachmentsV1ResponseMPayload

Response for GET /1/object/externalbroker/{pkiExternalbrokerID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachmentdocumenttype** | [**List[CustomAttachmentdocumenttypeResponse]**](CustomAttachmentdocumenttypeResponse.md) |  | 

## Example

```python
from eZmaxApi.models.externalbroker_get_attachments_v1_response_m_payload import ExternalbrokerGetAttachmentsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalbrokerGetAttachmentsV1ResponseMPayload from a JSON string
externalbroker_get_attachments_v1_response_m_payload_instance = ExternalbrokerGetAttachmentsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ExternalbrokerGetAttachmentsV1ResponseMPayload.to_json())

# convert the object into a dict
externalbroker_get_attachments_v1_response_m_payload_dict = externalbroker_get_attachments_v1_response_m_payload_instance.to_dict()
# create an instance of ExternalbrokerGetAttachmentsV1ResponseMPayload from a dict
externalbroker_get_attachments_v1_response_m_payload_from_dict = ExternalbrokerGetAttachmentsV1ResponseMPayload.from_dict(externalbroker_get_attachments_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


