# GlaccountGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/glaccount/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_glaccount** | [**List[GlaccountAutocompleteElementResponse]**](GlaccountAutocompleteElementResponse.md) | An array of Glaccount autocomplete element response. | 

## Example

```python
from eZmaxApi.models.glaccount_get_autocomplete_v2_response_m_payload import GlaccountGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of GlaccountGetAutocompleteV2ResponseMPayload from a JSON string
glaccount_get_autocomplete_v2_response_m_payload_instance = GlaccountGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(GlaccountGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
glaccount_get_autocomplete_v2_response_m_payload_dict = glaccount_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of GlaccountGetAutocompleteV2ResponseMPayload from a dict
glaccount_get_autocomplete_v2_response_m_payload_from_dict = GlaccountGetAutocompleteV2ResponseMPayload.from_dict(glaccount_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


