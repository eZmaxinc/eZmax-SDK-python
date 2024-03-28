# PhonetypeGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/phonetype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_phonetype** | [**List[PhonetypeAutocompleteElementResponse]**](PhonetypeAutocompleteElementResponse.md) | An array of Phonetype autocomplete element response. | 

## Example

```python
from eZmaxApi.models.phonetype_get_autocomplete_v2_response_m_payload import PhonetypeGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PhonetypeGetAutocompleteV2ResponseMPayload from a JSON string
phonetype_get_autocomplete_v2_response_m_payload_instance = PhonetypeGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PhonetypeGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
phonetype_get_autocomplete_v2_response_m_payload_dict = phonetype_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of PhonetypeGetAutocompleteV2ResponseMPayload from a dict
phonetype_get_autocomplete_v2_response_m_payload_form_dict = phonetype_get_autocomplete_v2_response_m_payload.from_dict(phonetype_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


