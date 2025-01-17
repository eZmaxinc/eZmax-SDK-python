# InvoiceGetCommunicationrecipientsV1Response

Response for GET /1/object/invoice/{pkiInvoiceID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**InvoiceGetCommunicationrecipientsV1ResponseMPayload**](InvoiceGetCommunicationrecipientsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.invoice_get_communicationrecipients_v1_response import InvoiceGetCommunicationrecipientsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceGetCommunicationrecipientsV1Response from a JSON string
invoice_get_communicationrecipients_v1_response_instance = InvoiceGetCommunicationrecipientsV1Response.from_json(json)
# print the JSON string representation of the object
print(InvoiceGetCommunicationrecipientsV1Response.to_json())

# convert the object into a dict
invoice_get_communicationrecipients_v1_response_dict = invoice_get_communicationrecipients_v1_response_instance.to_dict()
# create an instance of InvoiceGetCommunicationrecipientsV1Response from a dict
invoice_get_communicationrecipients_v1_response_from_dict = InvoiceGetCommunicationrecipientsV1Response.from_dict(invoice_get_communicationrecipients_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


