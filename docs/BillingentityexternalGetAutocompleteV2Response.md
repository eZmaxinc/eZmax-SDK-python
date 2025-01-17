# BillingentityexternalGetAutocompleteV2Response

Response for GET /2/object/billingentityexternal/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BillingentityexternalGetAutocompleteV2ResponseMPayload**](BillingentityexternalGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.billingentityexternal_get_autocomplete_v2_response import BillingentityexternalGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityexternalGetAutocompleteV2Response from a JSON string
billingentityexternal_get_autocomplete_v2_response_instance = BillingentityexternalGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(BillingentityexternalGetAutocompleteV2Response.to_json())

# convert the object into a dict
billingentityexternal_get_autocomplete_v2_response_dict = billingentityexternal_get_autocomplete_v2_response_instance.to_dict()
# create an instance of BillingentityexternalGetAutocompleteV2Response from a dict
billingentityexternal_get_autocomplete_v2_response_from_dict = BillingentityexternalGetAutocompleteV2Response.from_dict(billingentityexternal_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


