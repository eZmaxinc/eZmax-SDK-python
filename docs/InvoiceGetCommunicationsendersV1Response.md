# InvoiceGetCommunicationsendersV1Response

Response for GET /1/object/invoice/{pkiInvoiceID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InvoiceGetCommunicationsendersV1ResponseMPayload**](InvoiceGetCommunicationsendersV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.invoice_get_communicationsenders_v1_response import InvoiceGetCommunicationsendersV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceGetCommunicationsendersV1Response from a JSON string
invoice_get_communicationsenders_v1_response_instance = InvoiceGetCommunicationsendersV1Response.from_json(json)
# print the JSON string representation of the object
print(InvoiceGetCommunicationsendersV1Response.to_json())

# convert the object into a dict
invoice_get_communicationsenders_v1_response_dict = invoice_get_communicationsenders_v1_response_instance.to_dict()
# create an instance of InvoiceGetCommunicationsendersV1Response from a dict
invoice_get_communicationsenders_v1_response_from_dict = InvoiceGetCommunicationsendersV1Response.from_dict(invoice_get_communicationsenders_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


