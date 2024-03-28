# PaymenttermListElement

A Paymentterm List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_paymentterm_id** | **int** | The unique ID of the Paymentterm | 
**s_paymentterm_code** | **str** | The code of the Paymentterm | 
**e_paymentterm_type** | [**FieldEPaymenttermType**](FieldEPaymenttermType.md) |  | 
**i_paymentterm_day** | **int** | The day of the Paymentterm | 
**s_paymentterm_description_x** | **str** | The description of the Paymentterm in the language of the requester | 
**b_paymentterm_isactive** | **bool** | Whether the Paymentterm is active or not | 

## Example

```python
from eZmaxApi.models.paymentterm_list_element import PaymenttermListElement

# TODO update the JSON string below
json = "{}"
# create an instance of PaymenttermListElement from a JSON string
paymentterm_list_element_instance = PaymenttermListElement.from_json(json)
# print the JSON string representation of the object
print(PaymenttermListElement.to_json())

# convert the object into a dict
paymentterm_list_element_dict = paymentterm_list_element_instance.to_dict()
# create an instance of PaymenttermListElement from a dict
paymentterm_list_element_form_dict = paymentterm_list_element.from_dict(paymentterm_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


