# AgenttypeGetAutocompleteV2Response

Response for GET /2/object/agenttype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AgenttypeGetAutocompleteV2ResponseMPayload**](AgenttypeGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.agenttype_get_autocomplete_v2_response import AgenttypeGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of AgenttypeGetAutocompleteV2Response from a JSON string
agenttype_get_autocomplete_v2_response_instance = AgenttypeGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(AgenttypeGetAutocompleteV2Response.to_json())

# convert the object into a dict
agenttype_get_autocomplete_v2_response_dict = agenttype_get_autocomplete_v2_response_instance.to_dict()
# create an instance of AgenttypeGetAutocompleteV2Response from a dict
agenttype_get_autocomplete_v2_response_from_dict = AgenttypeGetAutocompleteV2Response.from_dict(agenttype_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


