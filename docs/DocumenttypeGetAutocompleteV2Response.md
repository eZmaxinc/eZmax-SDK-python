# DocumenttypeGetAutocompleteV2Response

Response for GET /2/object/documenttype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DocumenttypeGetAutocompleteV2ResponseMPayload**](DocumenttypeGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.documenttype_get_autocomplete_v2_response import DocumenttypeGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypeGetAutocompleteV2Response from a JSON string
documenttype_get_autocomplete_v2_response_instance = DocumenttypeGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(DocumenttypeGetAutocompleteV2Response.to_json())

# convert the object into a dict
documenttype_get_autocomplete_v2_response_dict = documenttype_get_autocomplete_v2_response_instance.to_dict()
# create an instance of DocumenttypeGetAutocompleteV2Response from a dict
documenttype_get_autocomplete_v2_response_from_dict = DocumenttypeGetAutocompleteV2Response.from_dict(documenttype_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


