# SupplierListElement

A Supplier List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_supplier_id** | **int** | The unique ID of the Supplier. | 
**fki_paymentmethod_id** | **int** | The unique ID of the Paymentmethod | [optional] 
**s_supplier_name** | **str** | The name of the Supplier | 
**s_supplier_code** | **str** | The code of the Supplier | 
**s_supplier_account** | **str** | The account of the Supplier | 
**b_supplier_isactive** | **bool** | Whether the supplier is active or not | 
**s_phone_e164** | **str** | A phone number in E.164 Format | [optional] 
**s_email_address** | **str** | The email address. | [optional] 
**s_address_civic** | **str** | The Civic number. | [optional] 
**s_address_street** | **str** | The Street Name | [optional] 
**s_address_suite** | **str** | The Suite or appartment number | [optional] 
**s_address_city** | **str** | The City name | [optional] 
**s_address_zip** | **str** | The Postal/Zip Code  The value must be entered without spaces | [optional] 
**s_province_name_x** | **str** | The name of the Province in the language of the requester | [optional] 
**s_country_name_x** | **str** | The name of the Country in the language of the requester | [optional] 
**s_paymentmethod_description_x** | **str** | The description of the Paymentmethod in the language of the requester | [optional] 
**s_electronicfundstransferbankaccount_transit** | **str** | The transit of the Electronicfundstransferbankaccount | [optional] 
**s_electronicfundstransferbankaccount_institution** | **str** | The institution of the Electronicfundstransferbankaccount | [optional] 
**s_electronicfundstransferbankaccount_account** | **str** | The account of the Electronicfundstransferbankaccount | [optional] 
**s_glaccountcontainer_longcode** | **str** | The Code for the Glaccountcontainer | 
**s_glaccountcontainer_longdescription_x** | **str** | The Description for the Glaccountcontainer in the language of the requester | 

## Example

```python
from eZmaxApi.models.supplier_list_element import SupplierListElement

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierListElement from a JSON string
supplier_list_element_instance = SupplierListElement.from_json(json)
# print the JSON string representation of the object
print(SupplierListElement.to_json())

# convert the object into a dict
supplier_list_element_dict = supplier_list_element_instance.to_dict()
# create an instance of SupplierListElement from a dict
supplier_list_element_from_dict = SupplierListElement.from_dict(supplier_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


