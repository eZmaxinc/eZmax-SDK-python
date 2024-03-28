# EzsignfoldertypeGetAutocompleteV2Response

Response for GET /2/object/ezsignfoldertype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfoldertypeGetAutocompleteV2ResponseMPayload**](EzsignfoldertypeGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_get_autocomplete_v2_response import EzsignfoldertypeGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeGetAutocompleteV2Response from a JSON string
ezsignfoldertype_get_autocomplete_v2_response_instance = EzsignfoldertypeGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeGetAutocompleteV2Response.to_json())

# convert the object into a dict
ezsignfoldertype_get_autocomplete_v2_response_dict = ezsignfoldertype_get_autocomplete_v2_response_instance.to_dict()
# create an instance of EzsignfoldertypeGetAutocompleteV2Response from a dict
ezsignfoldertype_get_autocomplete_v2_response_form_dict = ezsignfoldertype_get_autocomplete_v2_response.from_dict(ezsignfoldertype_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


