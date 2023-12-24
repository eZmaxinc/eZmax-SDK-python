# BillingentityinternalproductRequest

A Billingentityinternalproduct Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_billingentityinternalproduct_id** | **int** | The unique ID of the Billingentityinternalproduct | [optional] 
**fki_ezmaxproduct_id** | **int** | The unique ID of the Ezmaxproduct | 
**fki_billingentityexternal_id** | **int** | The unique ID of the Billingentityexternal | 

## Example

```python
from eZmaxApi.models.billingentityinternalproduct_request import BillingentityinternalproductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalproductRequest from a JSON string
billingentityinternalproduct_request_instance = BillingentityinternalproductRequest.from_json(json)
# print the JSON string representation of the object
print BillingentityinternalproductRequest.to_json()

# convert the object into a dict
billingentityinternalproduct_request_dict = billingentityinternalproduct_request_instance.to_dict()
# create an instance of BillingentityinternalproductRequest from a dict
billingentityinternalproduct_request_form_dict = billingentityinternalproduct_request.from_dict(billingentityinternalproduct_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


