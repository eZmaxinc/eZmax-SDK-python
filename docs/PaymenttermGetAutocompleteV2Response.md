# PaymenttermGetAutocompleteV2Response

Response for GET /2/object/paymentterm/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PaymenttermGetAutocompleteV2ResponseMPayload**](PaymenttermGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.paymentterm_get_autocomplete_v2_response import PaymenttermGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymenttermGetAutocompleteV2Response from a JSON string
paymentterm_get_autocomplete_v2_response_instance = PaymenttermGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(PaymenttermGetAutocompleteV2Response.to_json())

# convert the object into a dict
paymentterm_get_autocomplete_v2_response_dict = paymentterm_get_autocomplete_v2_response_instance.to_dict()
# create an instance of PaymenttermGetAutocompleteV2Response from a dict
paymentterm_get_autocomplete_v2_response_from_dict = PaymenttermGetAutocompleteV2Response.from_dict(paymentterm_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


