# TimezoneGetAutocompleteV2Response

Response for GET /2/object/timezone/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**TimezoneGetAutocompleteV2ResponseMPayload**](TimezoneGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.timezone_get_autocomplete_v2_response import TimezoneGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneGetAutocompleteV2Response from a JSON string
timezone_get_autocomplete_v2_response_instance = TimezoneGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(TimezoneGetAutocompleteV2Response.to_json())

# convert the object into a dict
timezone_get_autocomplete_v2_response_dict = timezone_get_autocomplete_v2_response_instance.to_dict()
# create an instance of TimezoneGetAutocompleteV2Response from a dict
timezone_get_autocomplete_v2_response_form_dict = timezone_get_autocomplete_v2_response.from_dict(timezone_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


