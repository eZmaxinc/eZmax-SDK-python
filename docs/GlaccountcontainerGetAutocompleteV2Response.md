# GlaccountcontainerGetAutocompleteV2Response

Response for GET /2/object/glaccountcontainer/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**GlaccountcontainerGetAutocompleteV2ResponseMPayload**](GlaccountcontainerGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.glaccountcontainer_get_autocomplete_v2_response import GlaccountcontainerGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of GlaccountcontainerGetAutocompleteV2Response from a JSON string
glaccountcontainer_get_autocomplete_v2_response_instance = GlaccountcontainerGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(GlaccountcontainerGetAutocompleteV2Response.to_json())

# convert the object into a dict
glaccountcontainer_get_autocomplete_v2_response_dict = glaccountcontainer_get_autocomplete_v2_response_instance.to_dict()
# create an instance of GlaccountcontainerGetAutocompleteV2Response from a dict
glaccountcontainer_get_autocomplete_v2_response_from_dict = GlaccountcontainerGetAutocompleteV2Response.from_dict(glaccountcontainer_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


