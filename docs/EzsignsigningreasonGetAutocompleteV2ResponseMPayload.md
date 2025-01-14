# EzsignsigningreasonGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/ezsignsigningreason/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignsigningreason** | [**List[EzsignsigningreasonAutocompleteElementResponse]**](EzsignsigningreasonAutocompleteElementResponse.md) | An array of Ezsignsigningreason autocomplete element response. | 

## Example

```python
from eZmaxApi.models.ezsignsigningreason_get_autocomplete_v2_response_m_payload import EzsignsigningreasonGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsigningreasonGetAutocompleteV2ResponseMPayload from a JSON string
ezsignsigningreason_get_autocomplete_v2_response_m_payload_instance = EzsignsigningreasonGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignsigningreasonGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
ezsignsigningreason_get_autocomplete_v2_response_m_payload_dict = ezsignsigningreason_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignsigningreasonGetAutocompleteV2ResponseMPayload from a dict
ezsignsigningreason_get_autocomplete_v2_response_m_payload_from_dict = EzsignsigningreasonGetAutocompleteV2ResponseMPayload.from_dict(ezsignsigningreason_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


