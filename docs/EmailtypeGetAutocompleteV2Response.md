# EmailtypeGetAutocompleteV2Response

Response for GET /2/object/emailtype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EmailtypeGetAutocompleteV2ResponseMPayload**](EmailtypeGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.emailtype_get_autocomplete_v2_response import EmailtypeGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EmailtypeGetAutocompleteV2Response from a JSON string
emailtype_get_autocomplete_v2_response_instance = EmailtypeGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(EmailtypeGetAutocompleteV2Response.to_json())

# convert the object into a dict
emailtype_get_autocomplete_v2_response_dict = emailtype_get_autocomplete_v2_response_instance.to_dict()
# create an instance of EmailtypeGetAutocompleteV2Response from a dict
emailtype_get_autocomplete_v2_response_form_dict = emailtype_get_autocomplete_v2_response.from_dict(emailtype_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


