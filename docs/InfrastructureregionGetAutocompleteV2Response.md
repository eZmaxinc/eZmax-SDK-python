# InfrastructureregionGetAutocompleteV2Response

Response for GET /2/object/infrastructureregion/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InfrastructureregionGetAutocompleteV2ResponseMPayload**](InfrastructureregionGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.infrastructureregion_get_autocomplete_v2_response import InfrastructureregionGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of InfrastructureregionGetAutocompleteV2Response from a JSON string
infrastructureregion_get_autocomplete_v2_response_instance = InfrastructureregionGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(InfrastructureregionGetAutocompleteV2Response.to_json())

# convert the object into a dict
infrastructureregion_get_autocomplete_v2_response_dict = infrastructureregion_get_autocomplete_v2_response_instance.to_dict()
# create an instance of InfrastructureregionGetAutocompleteV2Response from a dict
infrastructureregion_get_autocomplete_v2_response_from_dict = InfrastructureregionGetAutocompleteV2Response.from_dict(infrastructureregion_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


