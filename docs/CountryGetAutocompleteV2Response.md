# CountryGetAutocompleteV2Response

Response for GET /2/object/country/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CountryGetAutocompleteV2ResponseMPayload**](CountryGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.country_get_autocomplete_v2_response import CountryGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of CountryGetAutocompleteV2Response from a JSON string
country_get_autocomplete_v2_response_instance = CountryGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(CountryGetAutocompleteV2Response.to_json())

# convert the object into a dict
country_get_autocomplete_v2_response_dict = country_get_autocomplete_v2_response_instance.to_dict()
# create an instance of CountryGetAutocompleteV2Response from a dict
country_get_autocomplete_v2_response_form_dict = country_get_autocomplete_v2_response.from_dict(country_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


