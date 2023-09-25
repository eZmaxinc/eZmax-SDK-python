# BrandingGetAutocompleteV2Response

Response for GET /2/object/branding/getAutocomplete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BrandingGetAutocompleteV2ResponseMPayload**](BrandingGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.branding_get_autocomplete_v2_response import BrandingGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingGetAutocompleteV2Response from a JSON string
branding_get_autocomplete_v2_response_instance = BrandingGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print BrandingGetAutocompleteV2Response.to_json()

# convert the object into a dict
branding_get_autocomplete_v2_response_dict = branding_get_autocomplete_v2_response_instance.to_dict()
# create an instance of BrandingGetAutocompleteV2Response from a dict
branding_get_autocomplete_v2_response_form_dict = branding_get_autocomplete_v2_response.from_dict(branding_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


