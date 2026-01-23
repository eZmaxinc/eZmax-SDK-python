# SystemconfigurationtypeGetAutocompleteV2Response

Response for GET /2/object/systemconfigurationtype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SystemconfigurationtypeGetAutocompleteV2ResponseMPayload**](SystemconfigurationtypeGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.systemconfigurationtype_get_autocomplete_v2_response import SystemconfigurationtypeGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of SystemconfigurationtypeGetAutocompleteV2Response from a JSON string
systemconfigurationtype_get_autocomplete_v2_response_instance = SystemconfigurationtypeGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(SystemconfigurationtypeGetAutocompleteV2Response.to_json())

# convert the object into a dict
systemconfigurationtype_get_autocomplete_v2_response_dict = systemconfigurationtype_get_autocomplete_v2_response_instance.to_dict()
# create an instance of SystemconfigurationtypeGetAutocompleteV2Response from a dict
systemconfigurationtype_get_autocomplete_v2_response_from_dict = SystemconfigurationtypeGetAutocompleteV2Response.from_dict(systemconfigurationtype_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


