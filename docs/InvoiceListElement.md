# InvoiceListElement

A Invoice List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_invoice_id** | **int** | The unique ID of the Invoice. | 
**fki_agent_id** | **int** | The unique ID of the Agent. | [optional] 
**fki_broker_id** | **int** | The unique ID of the Broker. | [optional] 
**fki_customer_id** | **int** | The unique ID of the Customer. | [optional] 
**fki_period_id** | **int** | The unique ID of the Period | 
**s_period_yyyymm** | **str** | The YYYYMM of the Period | [optional] 
**b_invoice_ispaid** | **bool** | Whether if it&#39;s an ispaid | 
**d_invoice_total** | **str** | The total of the Invoice | 
**d_invoice_paid** | **str** | The paid of the Invoice | 
**d_invoice_balance** | **str** | The balance of the Invoice | [optional] 
**dt_invoice_date** | **str** | The date of the Invoice | 
**e_invoice_type** | [**FieldEInvoiceType**](FieldEInvoiceType.md) |  | 
**s_invoice_number** | **str** | The number of Invoice | [optional] 
**s_invoice_recipient** | **str** | The recipient of Invoice | [optional] 

## Example

```python
from eZmaxApi.models.invoice_list_element import InvoiceListElement

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceListElement from a JSON string
invoice_list_element_instance = InvoiceListElement.from_json(json)
# print the JSON string representation of the object
print(InvoiceListElement.to_json())

# convert the object into a dict
invoice_list_element_dict = invoice_list_element_instance.to_dict()
# create an instance of InvoiceListElement from a dict
invoice_list_element_from_dict = InvoiceListElement.from_dict(invoice_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


