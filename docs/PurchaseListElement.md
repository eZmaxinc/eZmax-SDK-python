# PurchaseListElement

A Purchase List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_purchase_id** | **int** | The unique ID of the Purchase | 
**fki_franchiseoffice_id** | **int** | The unique ID of the Franchisereoffice | [optional] 
**fki_supplier_id** | **int** | The unique ID of the Supplier. | [optional] 
**fki_period_id** | **int** | The unique ID of the Period | 
**s_purchase_billnumber** | **str** | The Billnumber of the Purchase | 
**dt_purchase_date** | **str** | The Date of the Purchase | 
**dt_purchase_paydate** | **str** | The Paydate of the Purchase | 
**d_purchase_total** | **str** | The Total of the Purchase | 
**b_purchase_isfinanced** | **bool** | Whether if it&#39;s an isfinanced | 
**b_purchase_ispaid** | **bool** | Whether if it&#39;s an ispaid | 
**s_franchiseagence_name** | **str** | The name of the Franchiseagence | [optional] 
**i_franchiseoffice_code** | **str** | The code of the Franchiseoffice | [optional] 
**s_supplier_name** | **str** | The name of the Supplier | [optional] 

## Example

```python
from eZmaxApi.models.purchase_list_element import PurchaseListElement

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseListElement from a JSON string
purchase_list_element_instance = PurchaseListElement.from_json(json)
# print the JSON string representation of the object
print(PurchaseListElement.to_json())

# convert the object into a dict
purchase_list_element_dict = purchase_list_element_instance.to_dict()
# create an instance of PurchaseListElement from a dict
purchase_list_element_from_dict = PurchaseListElement.from_dict(purchase_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


