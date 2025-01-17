# EzmaxproductGetAutocompleteV2Response

Response for GET /2/object/ezmaxproduct/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzmaxproductGetAutocompleteV2ResponseMPayload**](EzmaxproductGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxproduct_get_autocomplete_v2_response import EzmaxproductGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxproductGetAutocompleteV2Response from a JSON string
ezmaxproduct_get_autocomplete_v2_response_instance = EzmaxproductGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(EzmaxproductGetAutocompleteV2Response.to_json())

# convert the object into a dict
ezmaxproduct_get_autocomplete_v2_response_dict = ezmaxproduct_get_autocomplete_v2_response_instance.to_dict()
# create an instance of EzmaxproductGetAutocompleteV2Response from a dict
ezmaxproduct_get_autocomplete_v2_response_from_dict = EzmaxproductGetAutocompleteV2Response.from_dict(ezmaxproduct_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


