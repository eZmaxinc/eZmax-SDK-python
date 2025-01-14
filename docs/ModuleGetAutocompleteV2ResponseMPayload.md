# ModuleGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/module/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_module** | [**List[ModuleAutocompleteElementResponse]**](ModuleAutocompleteElementResponse.md) | An array of Module autocomplete element response. | 

## Example

```python
from eZmaxApi.models.module_get_autocomplete_v2_response_m_payload import ModuleGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleGetAutocompleteV2ResponseMPayload from a JSON string
module_get_autocomplete_v2_response_m_payload_instance = ModuleGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ModuleGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
module_get_autocomplete_v2_response_m_payload_dict = module_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of ModuleGetAutocompleteV2ResponseMPayload from a dict
module_get_autocomplete_v2_response_m_payload_from_dict = ModuleGetAutocompleteV2ResponseMPayload.from_dict(module_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


