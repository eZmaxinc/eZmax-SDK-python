# BillingentityinternalGetAutocompleteV2Response

Response for GET /2/object/billingentityinternal/getAutocomplete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BillingentityinternalGetAutocompleteV2ResponseMPayload**](BillingentityinternalGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.billingentityinternal_get_autocomplete_v2_response import BillingentityinternalGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalGetAutocompleteV2Response from a JSON string
billingentityinternal_get_autocomplete_v2_response_instance = BillingentityinternalGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print BillingentityinternalGetAutocompleteV2Response.to_json()

# convert the object into a dict
billingentityinternal_get_autocomplete_v2_response_dict = billingentityinternal_get_autocomplete_v2_response_instance.to_dict()
# create an instance of BillingentityinternalGetAutocompleteV2Response from a dict
billingentityinternal_get_autocomplete_v2_response_form_dict = billingentityinternal_get_autocomplete_v2_response.from_dict(billingentityinternal_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


