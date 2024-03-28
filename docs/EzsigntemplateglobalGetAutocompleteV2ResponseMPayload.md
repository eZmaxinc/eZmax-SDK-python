# EzsigntemplateglobalGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/ezsigntemplateglobal/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplateglobal** | [**List[EzsigntemplateglobalAutocompleteElementResponse]**](EzsigntemplateglobalAutocompleteElementResponse.md) | An array of Ezsigntemplateglobal autocomplete element response. | 

## Example

```python
from eZmaxApi.models.ezsigntemplateglobal_get_autocomplete_v2_response_m_payload import EzsigntemplateglobalGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateglobalGetAutocompleteV2ResponseMPayload from a JSON string
ezsigntemplateglobal_get_autocomplete_v2_response_m_payload_instance = EzsigntemplateglobalGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateglobalGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplateglobal_get_autocomplete_v2_response_m_payload_dict = ezsigntemplateglobal_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplateglobalGetAutocompleteV2ResponseMPayload from a dict
ezsigntemplateglobal_get_autocomplete_v2_response_m_payload_form_dict = ezsigntemplateglobal_get_autocomplete_v2_response_m_payload.from_dict(ezsigntemplateglobal_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


