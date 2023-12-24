# EzsigntemplateGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/ezsigntemplate/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplate** | [**List[EzsigntemplateAutocompleteElementResponse]**](EzsigntemplateAutocompleteElementResponse.md) | An array of Ezsigntemplate autocomplete element response. | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_get_autocomplete_v2_response_m_payload import EzsigntemplateGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateGetAutocompleteV2ResponseMPayload from a JSON string
ezsigntemplate_get_autocomplete_v2_response_m_payload_instance = EzsigntemplateGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateGetAutocompleteV2ResponseMPayload.to_json()

# convert the object into a dict
ezsigntemplate_get_autocomplete_v2_response_m_payload_dict = ezsigntemplate_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplateGetAutocompleteV2ResponseMPayload from a dict
ezsigntemplate_get_autocomplete_v2_response_m_payload_form_dict = ezsigntemplate_get_autocomplete_v2_response_m_payload.from_dict(ezsigntemplate_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


