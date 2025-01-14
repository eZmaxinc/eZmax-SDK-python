# PaymenttermResponse

A Paymentterm Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_paymentterm_id** | **int** | The unique ID of the Paymentterm | 
**s_paymentterm_code** | **str** | The code of the Paymentterm | 
**e_paymentterm_type** | [**FieldEPaymenttermType**](FieldEPaymenttermType.md) |  | 
**i_paymentterm_day** | **int** | The day of the Paymentterm | 
**obj_paymentterm_description** | [**MultilingualPaymenttermDescription**](MultilingualPaymenttermDescription.md) |  | 
**b_paymentterm_isactive** | **bool** | Whether the Paymentterm is active or not | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 

## Example

```python
from eZmaxApi.models.paymentterm_response import PaymenttermResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymenttermResponse from a JSON string
paymentterm_response_instance = PaymenttermResponse.from_json(json)
# print the JSON string representation of the object
print(PaymenttermResponse.to_json())

# convert the object into a dict
paymentterm_response_dict = paymentterm_response_instance.to_dict()
# create an instance of PaymenttermResponse from a dict
paymentterm_response_from_dict = PaymenttermResponse.from_dict(paymentterm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


