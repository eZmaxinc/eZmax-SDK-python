# UsergroupexternalGetAutocompleteV2Response

Response for GET /2/object/usergroupexternal/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UsergroupexternalGetAutocompleteV2ResponseMPayload**](UsergroupexternalGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupexternal_get_autocomplete_v2_response import UsergroupexternalGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalGetAutocompleteV2Response from a JSON string
usergroupexternal_get_autocomplete_v2_response_instance = UsergroupexternalGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalGetAutocompleteV2Response.to_json())

# convert the object into a dict
usergroupexternal_get_autocomplete_v2_response_dict = usergroupexternal_get_autocomplete_v2_response_instance.to_dict()
# create an instance of UsergroupexternalGetAutocompleteV2Response from a dict
usergroupexternal_get_autocomplete_v2_response_form_dict = usergroupexternal_get_autocomplete_v2_response.from_dict(usergroupexternal_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


