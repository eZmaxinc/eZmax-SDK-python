# FontGetAutocompleteV2Response

Response for GET /2/object/font/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**FontGetAutocompleteV2ResponseMPayload**](FontGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.font_get_autocomplete_v2_response import FontGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of FontGetAutocompleteV2Response from a JSON string
font_get_autocomplete_v2_response_instance = FontGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(FontGetAutocompleteV2Response.to_json())

# convert the object into a dict
font_get_autocomplete_v2_response_dict = font_get_autocomplete_v2_response_instance.to_dict()
# create an instance of FontGetAutocompleteV2Response from a dict
font_get_autocomplete_v2_response_from_dict = FontGetAutocompleteV2Response.from_dict(font_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


