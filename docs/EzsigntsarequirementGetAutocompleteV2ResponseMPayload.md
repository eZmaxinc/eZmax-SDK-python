# EzsigntsarequirementGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/ezsigntsarequirement/getAutocomplete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntsarequirement** | [**List[EzsigntsarequirementAutocompleteElementResponse]**](EzsigntsarequirementAutocompleteElementResponse.md) | An array of Ezsigntsarequirement autocomplete element response. | 

## Example

```python
from eZmaxApi.models.ezsigntsarequirement_get_autocomplete_v2_response_m_payload import EzsigntsarequirementGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntsarequirementGetAutocompleteV2ResponseMPayload from a JSON string
ezsigntsarequirement_get_autocomplete_v2_response_m_payload_instance = EzsigntsarequirementGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsigntsarequirementGetAutocompleteV2ResponseMPayload.to_json()

# convert the object into a dict
ezsigntsarequirement_get_autocomplete_v2_response_m_payload_dict = ezsigntsarequirement_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntsarequirementGetAutocompleteV2ResponseMPayload from a dict
ezsigntsarequirement_get_autocomplete_v2_response_m_payload_form_dict = ezsigntsarequirement_get_autocomplete_v2_response_m_payload.from_dict(ezsigntsarequirement_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


