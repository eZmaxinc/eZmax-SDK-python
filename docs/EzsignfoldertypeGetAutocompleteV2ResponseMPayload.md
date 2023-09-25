# EzsignfoldertypeGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/ezsignfoldertype/getAutocomplete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignfoldertype** | [**List[EzsignfoldertypeAutocompleteElementResponse]**](EzsignfoldertypeAutocompleteElementResponse.md) | An array of Ezsignfoldertype autocomplete element response. | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_get_autocomplete_v2_response_m_payload import EzsignfoldertypeGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeGetAutocompleteV2ResponseMPayload from a JSON string
ezsignfoldertype_get_autocomplete_v2_response_m_payload_instance = EzsignfoldertypeGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignfoldertypeGetAutocompleteV2ResponseMPayload.to_json()

# convert the object into a dict
ezsignfoldertype_get_autocomplete_v2_response_m_payload_dict = ezsignfoldertype_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignfoldertypeGetAutocompleteV2ResponseMPayload from a dict
ezsignfoldertype_get_autocomplete_v2_response_m_payload_form_dict = ezsignfoldertype_get_autocomplete_v2_response_m_payload.from_dict(ezsignfoldertype_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


