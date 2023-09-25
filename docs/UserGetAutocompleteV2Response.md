# UserGetAutocompleteV2Response

Response for GET /2/object/user/getAutocomplete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UserGetAutocompleteV2ResponseMPayload**](UserGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.user_get_autocomplete_v2_response import UserGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetAutocompleteV2Response from a JSON string
user_get_autocomplete_v2_response_instance = UserGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print UserGetAutocompleteV2Response.to_json()

# convert the object into a dict
user_get_autocomplete_v2_response_dict = user_get_autocomplete_v2_response_instance.to_dict()
# create an instance of UserGetAutocompleteV2Response from a dict
user_get_autocomplete_v2_response_form_dict = user_get_autocomplete_v2_response.from_dict(user_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


