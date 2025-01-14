# PdfalevelGetAutocompleteV2Response

Response for GET /2/object/pdfalevel/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PdfalevelGetAutocompleteV2ResponseMPayload**](PdfalevelGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.pdfalevel_get_autocomplete_v2_response import PdfalevelGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of PdfalevelGetAutocompleteV2Response from a JSON string
pdfalevel_get_autocomplete_v2_response_instance = PdfalevelGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(PdfalevelGetAutocompleteV2Response.to_json())

# convert the object into a dict
pdfalevel_get_autocomplete_v2_response_dict = pdfalevel_get_autocomplete_v2_response_instance.to_dict()
# create an instance of PdfalevelGetAutocompleteV2Response from a dict
pdfalevel_get_autocomplete_v2_response_from_dict = PdfalevelGetAutocompleteV2Response.from_dict(pdfalevel_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


