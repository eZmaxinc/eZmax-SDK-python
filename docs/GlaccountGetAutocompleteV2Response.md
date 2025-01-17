# GlaccountGetAutocompleteV2Response

Response for GET /2/object/glaccount/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**GlaccountGetAutocompleteV2ResponseMPayload**](GlaccountGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.glaccount_get_autocomplete_v2_response import GlaccountGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of GlaccountGetAutocompleteV2Response from a JSON string
glaccount_get_autocomplete_v2_response_instance = GlaccountGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(GlaccountGetAutocompleteV2Response.to_json())

# convert the object into a dict
glaccount_get_autocomplete_v2_response_dict = glaccount_get_autocomplete_v2_response_instance.to_dict()
# create an instance of GlaccountGetAutocompleteV2Response from a dict
glaccount_get_autocomplete_v2_response_from_dict = GlaccountGetAutocompleteV2Response.from_dict(glaccount_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


