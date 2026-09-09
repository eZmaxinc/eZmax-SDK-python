# BuyercontractResponse

A Buyercontract Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_buyercontract_id** | **int** | The unique ID of the Buyercontract | 
**fki_inscriptiontype_id** | **int** | The unique ID of the Inscriptiontype | 
**e_buyercontract_step** | [**FieldEBuyercontractStep**](FieldEBuyercontractStep.md) |  | 
**d_buyercontract_minimumprice** | **str** | The minimum price of the Buyercontract | 
**d_buyercontract_maximumprice** | **str** | The maximum price of the Buyercontract | 
**e_buyercontract_type** | [**FieldEBuyercontractType**](FieldEBuyercontractType.md) |  | 
**s_buyercontract_contract** | **str** | The number of the Buyercontract | [optional] 
**dt_buyercontract_date** | **str** | The date of the Buyercontract | 
**dt_buyercontract_expirationdate** | **str** | The expiration date of the Buyercontract | [optional] 
**d_buyercontract_remuneration** | **str** | The remuneration of the Buyercontract | [optional] 
**e_buyercontract_remunerationtype** | [**FieldEBuyercontractRemunerationtype**](FieldEBuyercontractRemunerationtype.md) |  | [optional] 
**b_buyercontract_litigation** | **bool** | Whether if it&#39;s an litigation | [optional] 
**b_buyercontract_isactive** | **bool** | Whether the buyercontract is active or not | 

## Example

```python
from eZmaxApi.models.buyercontract_response import BuyercontractResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractResponse from a JSON string
buyercontract_response_instance = BuyercontractResponse.from_json(json)
# print the JSON string representation of the object
print(BuyercontractResponse.to_json())

# convert the object into a dict
buyercontract_response_dict = buyercontract_response_instance.to_dict()
# create an instance of BuyercontractResponse from a dict
buyercontract_response_from_dict = BuyercontractResponse.from_dict(buyercontract_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


