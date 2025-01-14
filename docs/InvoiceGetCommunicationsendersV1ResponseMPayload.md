# InvoiceGetCommunicationsendersV1ResponseMPayload

Response for GET /1/object/invoice/{pkiInvoiceID}/getCommunicationsenders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationsenders** | [**List[CustomCommunicationsenderResponse]**](CustomCommunicationsenderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.invoice_get_communicationsenders_v1_response_m_payload import InvoiceGetCommunicationsendersV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceGetCommunicationsendersV1ResponseMPayload from a JSON string
invoice_get_communicationsenders_v1_response_m_payload_instance = InvoiceGetCommunicationsendersV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InvoiceGetCommunicationsendersV1ResponseMPayload.to_json())

# convert the object into a dict
invoice_get_communicationsenders_v1_response_m_payload_dict = invoice_get_communicationsenders_v1_response_m_payload_instance.to_dict()
# create an instance of InvoiceGetCommunicationsendersV1ResponseMPayload from a dict
invoice_get_communicationsenders_v1_response_m_payload_from_dict = InvoiceGetCommunicationsendersV1ResponseMPayload.from_dict(invoice_get_communicationsenders_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


