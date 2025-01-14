# EzsigntsarequirementGetAutocompleteV2Response

Response for GET /2/object/ezsigntsarequirement/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntsarequirementGetAutocompleteV2ResponseMPayload**](EzsigntsarequirementGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntsarequirement_get_autocomplete_v2_response import EzsigntsarequirementGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntsarequirementGetAutocompleteV2Response from a JSON string
ezsigntsarequirement_get_autocomplete_v2_response_instance = EzsigntsarequirementGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntsarequirementGetAutocompleteV2Response.to_json())

# convert the object into a dict
ezsigntsarequirement_get_autocomplete_v2_response_dict = ezsigntsarequirement_get_autocomplete_v2_response_instance.to_dict()
# create an instance of EzsigntsarequirementGetAutocompleteV2Response from a dict
ezsigntsarequirement_get_autocomplete_v2_response_from_dict = EzsigntsarequirementGetAutocompleteV2Response.from_dict(ezsigntsarequirement_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


