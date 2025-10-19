# OtherincometypeGetAutocompleteV2Response

Response for GET /2/object/otherincometype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**OtherincometypeGetAutocompleteV2ResponseMPayload**](OtherincometypeGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.otherincometype_get_autocomplete_v2_response import OtherincometypeGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of OtherincometypeGetAutocompleteV2Response from a JSON string
otherincometype_get_autocomplete_v2_response_instance = OtherincometypeGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(OtherincometypeGetAutocompleteV2Response.to_json())

# convert the object into a dict
otherincometype_get_autocomplete_v2_response_dict = otherincometype_get_autocomplete_v2_response_instance.to_dict()
# create an instance of OtherincometypeGetAutocompleteV2Response from a dict
otherincometype_get_autocomplete_v2_response_from_dict = OtherincometypeGetAutocompleteV2Response.from_dict(otherincometype_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


