# SupplyGetAutocompleteV2Response

Response for GET /2/object/supply/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SupplyGetAutocompleteV2ResponseMPayload**](SupplyGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.supply_get_autocomplete_v2_response import SupplyGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyGetAutocompleteV2Response from a JSON string
supply_get_autocomplete_v2_response_instance = SupplyGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(SupplyGetAutocompleteV2Response.to_json())

# convert the object into a dict
supply_get_autocomplete_v2_response_dict = supply_get_autocomplete_v2_response_instance.to_dict()
# create an instance of SupplyGetAutocompleteV2Response from a dict
supply_get_autocomplete_v2_response_from_dict = SupplyGetAutocompleteV2Response.from_dict(supply_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


