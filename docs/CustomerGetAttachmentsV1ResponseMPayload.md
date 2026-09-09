# CustomerGetAttachmentsV1ResponseMPayload

Response for GET /1/object/customer/{pkiCustomerID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachmentdocumenttype** | [**List[CustomAttachmentdocumenttypeResponse]**](CustomAttachmentdocumenttypeResponse.md) |  | 

## Example

```python
from eZmaxApi.models.customer_get_attachments_v1_response_m_payload import CustomerGetAttachmentsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetAttachmentsV1ResponseMPayload from a JSON string
customer_get_attachments_v1_response_m_payload_instance = CustomerGetAttachmentsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CustomerGetAttachmentsV1ResponseMPayload.to_json())

# convert the object into a dict
customer_get_attachments_v1_response_m_payload_dict = customer_get_attachments_v1_response_m_payload_instance.to_dict()
# create an instance of CustomerGetAttachmentsV1ResponseMPayload from a dict
customer_get_attachments_v1_response_m_payload_from_dict = CustomerGetAttachmentsV1ResponseMPayload.from_dict(customer_get_attachments_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


