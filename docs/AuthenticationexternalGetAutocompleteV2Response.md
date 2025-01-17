# AuthenticationexternalGetAutocompleteV2Response

Response for GET /2/object/authenticationexternal/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AuthenticationexternalGetAutocompleteV2ResponseMPayload**](AuthenticationexternalGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.authenticationexternal_get_autocomplete_v2_response import AuthenticationexternalGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalGetAutocompleteV2Response from a JSON string
authenticationexternal_get_autocomplete_v2_response_instance = AuthenticationexternalGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalGetAutocompleteV2Response.to_json())

# convert the object into a dict
authenticationexternal_get_autocomplete_v2_response_dict = authenticationexternal_get_autocomplete_v2_response_instance.to_dict()
# create an instance of AuthenticationexternalGetAutocompleteV2Response from a dict
authenticationexternal_get_autocomplete_v2_response_from_dict = AuthenticationexternalGetAutocompleteV2Response.from_dict(authenticationexternal_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


