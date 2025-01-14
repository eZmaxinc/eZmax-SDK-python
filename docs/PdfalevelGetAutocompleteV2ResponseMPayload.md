# PdfalevelGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/pdfalevel/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_pdfalevel** | [**List[PdfalevelAutocompleteElementResponse]**](PdfalevelAutocompleteElementResponse.md) | An array of Pdfalevel autocomplete element response. | 

## Example

```python
from eZmaxApi.models.pdfalevel_get_autocomplete_v2_response_m_payload import PdfalevelGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PdfalevelGetAutocompleteV2ResponseMPayload from a JSON string
pdfalevel_get_autocomplete_v2_response_m_payload_instance = PdfalevelGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PdfalevelGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
pdfalevel_get_autocomplete_v2_response_m_payload_dict = pdfalevel_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of PdfalevelGetAutocompleteV2ResponseMPayload from a dict
pdfalevel_get_autocomplete_v2_response_m_payload_from_dict = PdfalevelGetAutocompleteV2ResponseMPayload.from_dict(pdfalevel_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


