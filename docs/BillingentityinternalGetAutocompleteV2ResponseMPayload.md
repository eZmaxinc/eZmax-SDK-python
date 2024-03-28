# BillingentityinternalGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/billingentityinternal/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_billingentityinternal** | [**List[BillingentityinternalAutocompleteElementResponse]**](BillingentityinternalAutocompleteElementResponse.md) | An array of Billingentityinternal object containing the description, ID and active status about the element. | 

## Example

```python
from eZmaxApi.models.billingentityinternal_get_autocomplete_v2_response_m_payload import BillingentityinternalGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalGetAutocompleteV2ResponseMPayload from a JSON string
billingentityinternal_get_autocomplete_v2_response_m_payload_instance = BillingentityinternalGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BillingentityinternalGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
billingentityinternal_get_autocomplete_v2_response_m_payload_dict = billingentityinternal_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of BillingentityinternalGetAutocompleteV2ResponseMPayload from a dict
billingentityinternal_get_autocomplete_v2_response_m_payload_form_dict = billingentityinternal_get_autocomplete_v2_response_m_payload.from_dict(billingentityinternal_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


