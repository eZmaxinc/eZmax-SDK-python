# EmailtypeGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/emailtype/getAutocomplete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_emailtype** | [**List[EmailtypeAutocompleteElementResponse]**](EmailtypeAutocompleteElementResponse.md) | An array of Emailtype autocomplete element response. | 

## Example

```python
from eZmaxApi.models.emailtype_get_autocomplete_v2_response_m_payload import EmailtypeGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EmailtypeGetAutocompleteV2ResponseMPayload from a JSON string
emailtype_get_autocomplete_v2_response_m_payload_instance = EmailtypeGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EmailtypeGetAutocompleteV2ResponseMPayload.to_json()

# convert the object into a dict
emailtype_get_autocomplete_v2_response_m_payload_dict = emailtype_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of EmailtypeGetAutocompleteV2ResponseMPayload from a dict
emailtype_get_autocomplete_v2_response_m_payload_form_dict = emailtype_get_autocomplete_v2_response_m_payload.from_dict(emailtype_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


