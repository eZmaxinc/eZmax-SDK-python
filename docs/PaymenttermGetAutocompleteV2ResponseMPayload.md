# PaymenttermGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/paymentterm/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_paymentterm** | [**List[PaymenttermAutocompleteElementResponse]**](PaymenttermAutocompleteElementResponse.md) | An array of Paymentterm autocomplete element response. | 

## Example

```python
from eZmaxApi.models.paymentterm_get_autocomplete_v2_response_m_payload import PaymenttermGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PaymenttermGetAutocompleteV2ResponseMPayload from a JSON string
paymentterm_get_autocomplete_v2_response_m_payload_instance = PaymenttermGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print PaymenttermGetAutocompleteV2ResponseMPayload.to_json()

# convert the object into a dict
paymentterm_get_autocomplete_v2_response_m_payload_dict = paymentterm_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of PaymenttermGetAutocompleteV2ResponseMPayload from a dict
paymentterm_get_autocomplete_v2_response_m_payload_form_dict = paymentterm_get_autocomplete_v2_response_m_payload.from_dict(paymentterm_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


