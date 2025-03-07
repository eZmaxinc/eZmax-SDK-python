# PaymentgatewayGetAutocompleteV2Response

Response for GET /2/object/paymentgateway/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PaymentgatewayGetAutocompleteV2ResponseMPayload**](PaymentgatewayGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.paymentgateway_get_autocomplete_v2_response import PaymentgatewayGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentgatewayGetAutocompleteV2Response from a JSON string
paymentgateway_get_autocomplete_v2_response_instance = PaymentgatewayGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(PaymentgatewayGetAutocompleteV2Response.to_json())

# convert the object into a dict
paymentgateway_get_autocomplete_v2_response_dict = paymentgateway_get_autocomplete_v2_response_instance.to_dict()
# create an instance of PaymentgatewayGetAutocompleteV2Response from a dict
paymentgateway_get_autocomplete_v2_response_from_dict = PaymentgatewayGetAutocompleteV2Response.from_dict(paymentgateway_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


