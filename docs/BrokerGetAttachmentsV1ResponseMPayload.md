# BrokerGetAttachmentsV1ResponseMPayload

Response for GET /1/object/broker/{pkiBrokerID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachmentdocumenttype** | [**List[CustomAttachmentdocumenttypeResponse]**](CustomAttachmentdocumenttypeResponse.md) |  | 

## Example

```python
from eZmaxApi.models.broker_get_attachments_v1_response_m_payload import BrokerGetAttachmentsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerGetAttachmentsV1ResponseMPayload from a JSON string
broker_get_attachments_v1_response_m_payload_instance = BrokerGetAttachmentsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BrokerGetAttachmentsV1ResponseMPayload.to_json())

# convert the object into a dict
broker_get_attachments_v1_response_m_payload_dict = broker_get_attachments_v1_response_m_payload_instance.to_dict()
# create an instance of BrokerGetAttachmentsV1ResponseMPayload from a dict
broker_get_attachments_v1_response_m_payload_from_dict = BrokerGetAttachmentsV1ResponseMPayload.from_dict(broker_get_attachments_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


