# GlaccountcontainerGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/glaccountcontainer/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_glaccountcontainer** | [**List[GlaccountcontainerAutocompleteElementResponse]**](GlaccountcontainerAutocompleteElementResponse.md) | An array of Glaccountcontainer autocomplete element response. | 

## Example

```python
from eZmaxApi.models.glaccountcontainer_get_autocomplete_v2_response_m_payload import GlaccountcontainerGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of GlaccountcontainerGetAutocompleteV2ResponseMPayload from a JSON string
glaccountcontainer_get_autocomplete_v2_response_m_payload_instance = GlaccountcontainerGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(GlaccountcontainerGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
glaccountcontainer_get_autocomplete_v2_response_m_payload_dict = glaccountcontainer_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of GlaccountcontainerGetAutocompleteV2ResponseMPayload from a dict
glaccountcontainer_get_autocomplete_v2_response_m_payload_from_dict = GlaccountcontainerGetAutocompleteV2ResponseMPayload.from_dict(glaccountcontainer_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


