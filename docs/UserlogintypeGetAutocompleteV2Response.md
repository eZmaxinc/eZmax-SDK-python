# UserlogintypeGetAutocompleteV2Response

Response for GET /2/object/userlogintype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UserlogintypeGetAutocompleteV2ResponseMPayload**](UserlogintypeGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.userlogintype_get_autocomplete_v2_response import UserlogintypeGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserlogintypeGetAutocompleteV2Response from a JSON string
userlogintype_get_autocomplete_v2_response_instance = UserlogintypeGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(UserlogintypeGetAutocompleteV2Response.to_json())

# convert the object into a dict
userlogintype_get_autocomplete_v2_response_dict = userlogintype_get_autocomplete_v2_response_instance.to_dict()
# create an instance of UserlogintypeGetAutocompleteV2Response from a dict
userlogintype_get_autocomplete_v2_response_form_dict = userlogintype_get_autocomplete_v2_response.from_dict(userlogintype_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


