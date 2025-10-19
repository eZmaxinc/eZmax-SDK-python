# BuyercontractListElement

A Buyercontract List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_buyercontract_id** | **int** | The unique ID of the Buyercontract | 
**fki_inscriptiontype_id** | **int** | The unique ID of the Inscriptiontype | 
**s_inscriptiontype_name_x** | **str** | The name of the Inscriptiontype in the language of the requester | 
**e_buyercontract_step** | [**FieldEBuyercontractStep**](FieldEBuyercontractStep.md) |  | 
**d_buyercontract_minimumprice** | **str** | The minimumprice of the Buyercontract | 
**d_buyercontract_maximumprice** | **str** | The maximumprice of the Buyercontract | 
**e_buyercontract_type** | [**FieldEBuyercontractType**](FieldEBuyercontractType.md) |  | 
**dt_buyercontract_date** | **str** | The date of the Buyercontract | 
**dt_buyercontract_expirationdate** | **str** | The expirationdate of the Buyercontract | [optional] 
**b_buyercontract_isactive** | **bool** | Whether the buyercontract is active or not | 
**s_buyercontract_brokers** | **str** | The brokers&#39; name of the Buyercontract | 
**s_buyercontract_buyers** | **str** | The buyers&#39; name of the Buyercontract | 

## Example

```python
from eZmaxApi.models.buyercontract_list_element import BuyercontractListElement

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractListElement from a JSON string
buyercontract_list_element_instance = BuyercontractListElement.from_json(json)
# print the JSON string representation of the object
print(BuyercontractListElement.to_json())

# convert the object into a dict
buyercontract_list_element_dict = buyercontract_list_element_instance.to_dict()
# create an instance of BuyercontractListElement from a dict
buyercontract_list_element_from_dict = BuyercontractListElement.from_dict(buyercontract_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


