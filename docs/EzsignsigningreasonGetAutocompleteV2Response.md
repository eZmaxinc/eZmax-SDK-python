# EzsignsigningreasonGetAutocompleteV2Response

Response for GET /2/object/ezsignsigningreason/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignsigningreasonGetAutocompleteV2ResponseMPayload**](EzsignsigningreasonGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsigningreason_get_autocomplete_v2_response import EzsignsigningreasonGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsigningreasonGetAutocompleteV2Response from a JSON string
ezsignsigningreason_get_autocomplete_v2_response_instance = EzsignsigningreasonGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print EzsignsigningreasonGetAutocompleteV2Response.to_json()

# convert the object into a dict
ezsignsigningreason_get_autocomplete_v2_response_dict = ezsignsigningreason_get_autocomplete_v2_response_instance.to_dict()
# create an instance of EzsignsigningreasonGetAutocompleteV2Response from a dict
ezsignsigningreason_get_autocomplete_v2_response_form_dict = ezsignsigningreason_get_autocomplete_v2_response.from_dict(ezsignsigningreason_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


