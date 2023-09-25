# BillingentityexternalGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/billingentityexternal/getAutocomplete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_billingentityexternal** | [**List[BillingentityexternalAutocompleteElementResponse]**](BillingentityexternalAutocompleteElementResponse.md) | An array of Billingentityexternal autocomplete element response. | [optional] 

## Example

```python
from eZmaxApi.models.billingentityexternal_get_autocomplete_v2_response_m_payload import BillingentityexternalGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityexternalGetAutocompleteV2ResponseMPayload from a JSON string
billingentityexternal_get_autocomplete_v2_response_m_payload_instance = BillingentityexternalGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print BillingentityexternalGetAutocompleteV2ResponseMPayload.to_json()

# convert the object into a dict
billingentityexternal_get_autocomplete_v2_response_m_payload_dict = billingentityexternal_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of BillingentityexternalGetAutocompleteV2ResponseMPayload from a dict
billingentityexternal_get_autocomplete_v2_response_m_payload_form_dict = billingentityexternal_get_autocomplete_v2_response_m_payload.from_dict(billingentityexternal_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


