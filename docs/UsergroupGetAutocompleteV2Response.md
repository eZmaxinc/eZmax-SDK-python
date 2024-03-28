# UsergroupGetAutocompleteV2Response

Response for GET /2/object/usergroup/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UsergroupGetAutocompleteV2ResponseMPayload**](UsergroupGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_get_autocomplete_v2_response import UsergroupGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupGetAutocompleteV2Response from a JSON string
usergroup_get_autocomplete_v2_response_instance = UsergroupGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupGetAutocompleteV2Response.to_json())

# convert the object into a dict
usergroup_get_autocomplete_v2_response_dict = usergroup_get_autocomplete_v2_response_instance.to_dict()
# create an instance of UsergroupGetAutocompleteV2Response from a dict
usergroup_get_autocomplete_v2_response_form_dict = usergroup_get_autocomplete_v2_response.from_dict(usergroup_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


