# CreditcardtypeGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/creditcardtype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_creditcardtype** | [**List[CreditcardtypeAutocompleteElementResponse]**](CreditcardtypeAutocompleteElementResponse.md) | An array of Creditcardtype object containing the description, ID and active status about the element. | 

## Example

```python
from eZmaxApi.models.creditcardtype_get_autocomplete_v2_response_m_payload import CreditcardtypeGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardtypeGetAutocompleteV2ResponseMPayload from a JSON string
creditcardtype_get_autocomplete_v2_response_m_payload_instance = CreditcardtypeGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CreditcardtypeGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
creditcardtype_get_autocomplete_v2_response_m_payload_dict = creditcardtype_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of CreditcardtypeGetAutocompleteV2ResponseMPayload from a dict
creditcardtype_get_autocomplete_v2_response_m_payload_form_dict = creditcardtype_get_autocomplete_v2_response_m_payload.from_dict(creditcardtype_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


