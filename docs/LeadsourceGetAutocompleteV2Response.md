# LeadsourceGetAutocompleteV2Response

Response for GET /2/object/leadsource/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**LeadsourceGetAutocompleteV2ResponseMPayload**](LeadsourceGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.leadsource_get_autocomplete_v2_response import LeadsourceGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of LeadsourceGetAutocompleteV2Response from a JSON string
leadsource_get_autocomplete_v2_response_instance = LeadsourceGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(LeadsourceGetAutocompleteV2Response.to_json())

# convert the object into a dict
leadsource_get_autocomplete_v2_response_dict = leadsource_get_autocomplete_v2_response_instance.to_dict()
# create an instance of LeadsourceGetAutocompleteV2Response from a dict
leadsource_get_autocomplete_v2_response_from_dict = LeadsourceGetAutocompleteV2Response.from_dict(leadsource_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


