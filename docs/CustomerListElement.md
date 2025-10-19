# CustomerListElement

A Customer List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_customer_id** | **int** | The unique ID of the Customer. | 
**s_customer_name** | **str** | The name of the Customer | 
**s_customer_note** | **str** | A note for the Customer | [optional] 
**s_customer_code** | **str** | The code of the Customer | 
**b_customer_isactive** | **bool** | Whether the customer is active or not | 
**s_phone_e164** | **str** | A phone number in E.164 Format | [optional] 
**s_email_address** | **str** | The email address. | [optional] 
**s_address_civic** | **str** | The Civic number. | [optional] 
**s_address_street** | **str** | The Street Name | [optional] 
**s_address_suite** | **str** | The Suite or appartment number | [optional] 
**s_address_city** | **str** | The City name | [optional] 
**s_address_zip** | **str** | The Postal/Zip Code  The value must be entered without spaces | [optional] 
**s_province_name_x** | **str** | The name of the Province in the language of the requester | [optional] 
**s_country_name_x** | **str** | The name of the Country in the language of the requester | [optional] 

## Example

```python
from eZmaxApi.models.customer_list_element import CustomerListElement

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerListElement from a JSON string
customer_list_element_instance = CustomerListElement.from_json(json)
# print the JSON string representation of the object
print(CustomerListElement.to_json())

# convert the object into a dict
customer_list_element_dict = customer_list_element_instance.to_dict()
# create an instance of CustomerListElement from a dict
customer_list_element_from_dict = CustomerListElement.from_dict(customer_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


