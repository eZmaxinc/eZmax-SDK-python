# EzsigntemplateGetAutocompleteV2Response

Response for GET /2/object/ezsigntemplate/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplateGetAutocompleteV2ResponseMPayload**](EzsigntemplateGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_get_autocomplete_v2_response import EzsigntemplateGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateGetAutocompleteV2Response from a JSON string
ezsigntemplate_get_autocomplete_v2_response_instance = EzsigntemplateGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateGetAutocompleteV2Response.to_json()

# convert the object into a dict
ezsigntemplate_get_autocomplete_v2_response_dict = ezsigntemplate_get_autocomplete_v2_response_instance.to_dict()
# create an instance of EzsigntemplateGetAutocompleteV2Response from a dict
ezsigntemplate_get_autocomplete_v2_response_form_dict = ezsigntemplate_get_autocomplete_v2_response.from_dict(ezsigntemplate_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


