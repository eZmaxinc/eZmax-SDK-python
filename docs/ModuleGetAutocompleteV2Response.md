# ModuleGetAutocompleteV2Response

Response for GET /2/object/module/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**ModuleGetAutocompleteV2ResponseMPayload**](ModuleGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.module_get_autocomplete_v2_response import ModuleGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleGetAutocompleteV2Response from a JSON string
module_get_autocomplete_v2_response_instance = ModuleGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(ModuleGetAutocompleteV2Response.to_json())

# convert the object into a dict
module_get_autocomplete_v2_response_dict = module_get_autocomplete_v2_response_instance.to_dict()
# create an instance of ModuleGetAutocompleteV2Response from a dict
module_get_autocomplete_v2_response_from_dict = ModuleGetAutocompleteV2Response.from_dict(module_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


