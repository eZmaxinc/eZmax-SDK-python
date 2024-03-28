# FontGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/font/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_font** | [**List[FontAutocompleteElementResponse]**](FontAutocompleteElementResponse.md) | An array of Font autocomplete element response. | 

## Example

```python
from eZmaxApi.models.font_get_autocomplete_v2_response_m_payload import FontGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of FontGetAutocompleteV2ResponseMPayload from a JSON string
font_get_autocomplete_v2_response_m_payload_instance = FontGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(FontGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
font_get_autocomplete_v2_response_m_payload_dict = font_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of FontGetAutocompleteV2ResponseMPayload from a dict
font_get_autocomplete_v2_response_m_payload_form_dict = font_get_autocomplete_v2_response_m_payload.from_dict(font_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


