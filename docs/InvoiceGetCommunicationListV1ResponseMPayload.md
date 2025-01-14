# InvoiceGetCommunicationListV1ResponseMPayload

Response for GET /1/object/invoice/{pkiInvoiceID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communication** | [**List[CustomCommunicationListElementResponse]**](CustomCommunicationListElementResponse.md) |  | 

## Example

```python
from eZmaxApi.models.invoice_get_communication_list_v1_response_m_payload import InvoiceGetCommunicationListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceGetCommunicationListV1ResponseMPayload from a JSON string
invoice_get_communication_list_v1_response_m_payload_instance = InvoiceGetCommunicationListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InvoiceGetCommunicationListV1ResponseMPayload.to_json())

# convert the object into a dict
invoice_get_communication_list_v1_response_m_payload_dict = invoice_get_communication_list_v1_response_m_payload_instance.to_dict()
# create an instance of InvoiceGetCommunicationListV1ResponseMPayload from a dict
invoice_get_communication_list_v1_response_m_payload_from_dict = InvoiceGetCommunicationListV1ResponseMPayload.from_dict(invoice_get_communication_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


