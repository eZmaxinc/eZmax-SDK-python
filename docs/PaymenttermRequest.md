# PaymenttermRequest

A Paymentterm Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_paymentterm_id** | **int** | The unique ID of the Paymentterm | [optional] 
**s_paymentterm_code** | **str** | The code of the Paymentterm | 
**e_paymentterm_type** | [**FieldEPaymenttermType**](FieldEPaymenttermType.md) |  | 
**i_paymentterm_day** | **int** | The day of the Paymentterm | 
**obj_paymentterm_description** | [**MultilingualPaymenttermDescription**](MultilingualPaymenttermDescription.md) |  | 
**b_paymentterm_isactive** | **bool** | Whether the Paymentterm is active or not | 

## Example

```python
from eZmaxApi.models.paymentterm_request import PaymenttermRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymenttermRequest from a JSON string
paymentterm_request_instance = PaymenttermRequest.from_json(json)
# print the JSON string representation of the object
print(PaymenttermRequest.to_json())

# convert the object into a dict
paymentterm_request_dict = paymentterm_request_instance.to_dict()
# create an instance of PaymenttermRequest from a dict
paymentterm_request_form_dict = paymentterm_request.from_dict(paymentterm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


