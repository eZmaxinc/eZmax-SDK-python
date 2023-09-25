# PaymenttermResponseCompound

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
from eZmaxApi.models.paymentterm_response_compound import PaymenttermResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of PaymenttermResponseCompound from a JSON string
paymentterm_response_compound_instance = PaymenttermResponseCompound.from_json(json)
# print the JSON string representation of the object
print PaymenttermResponseCompound.to_json()

# convert the object into a dict
paymentterm_response_compound_dict = paymentterm_response_compound_instance.to_dict()
# create an instance of PaymenttermResponseCompound from a dict
paymentterm_response_compound_form_dict = paymentterm_response_compound.from_dict(paymentterm_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


