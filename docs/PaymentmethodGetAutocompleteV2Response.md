# PaymentmethodGetAutocompleteV2Response

Response for GET /2/object/paymentmethod/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PaymentmethodGetAutocompleteV2ResponseMPayload**](PaymentmethodGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.paymentmethod_get_autocomplete_v2_response import PaymentmethodGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentmethodGetAutocompleteV2Response from a JSON string
paymentmethod_get_autocomplete_v2_response_instance = PaymentmethodGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(PaymentmethodGetAutocompleteV2Response.to_json())

# convert the object into a dict
paymentmethod_get_autocomplete_v2_response_dict = paymentmethod_get_autocomplete_v2_response_instance.to_dict()
# create an instance of PaymentmethodGetAutocompleteV2Response from a dict
paymentmethod_get_autocomplete_v2_response_from_dict = PaymentmethodGetAutocompleteV2Response.from_dict(paymentmethod_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


