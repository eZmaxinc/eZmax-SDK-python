# ProvinceGetAutocompleteV2Response

Response for GET /2/object/province/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ProvinceGetAutocompleteV2ResponseMPayload**](ProvinceGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.province_get_autocomplete_v2_response import ProvinceGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProvinceGetAutocompleteV2Response from a JSON string
province_get_autocomplete_v2_response_instance = ProvinceGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(ProvinceGetAutocompleteV2Response.to_json())

# convert the object into a dict
province_get_autocomplete_v2_response_dict = province_get_autocomplete_v2_response_instance.to_dict()
# create an instance of ProvinceGetAutocompleteV2Response from a dict
province_get_autocomplete_v2_response_form_dict = province_get_autocomplete_v2_response.from_dict(province_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


