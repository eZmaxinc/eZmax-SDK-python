# RealestateboardGetAutocompleteV2Response

Response for GET /2/object/realestateboard/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**RealestateboardGetAutocompleteV2ResponseMPayload**](RealestateboardGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.realestateboard_get_autocomplete_v2_response import RealestateboardGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of RealestateboardGetAutocompleteV2Response from a JSON string
realestateboard_get_autocomplete_v2_response_instance = RealestateboardGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(RealestateboardGetAutocompleteV2Response.to_json())

# convert the object into a dict
realestateboard_get_autocomplete_v2_response_dict = realestateboard_get_autocomplete_v2_response_instance.to_dict()
# create an instance of RealestateboardGetAutocompleteV2Response from a dict
realestateboard_get_autocomplete_v2_response_from_dict = RealestateboardGetAutocompleteV2Response.from_dict(realestateboard_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


