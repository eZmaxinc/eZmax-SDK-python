# PeriodGetAutocompleteV2Response

Response for GET /2/object/period/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PeriodGetAutocompleteV2ResponseMPayload**](PeriodGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.period_get_autocomplete_v2_response import PeriodGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodGetAutocompleteV2Response from a JSON string
period_get_autocomplete_v2_response_instance = PeriodGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(PeriodGetAutocompleteV2Response.to_json())

# convert the object into a dict
period_get_autocomplete_v2_response_dict = period_get_autocomplete_v2_response_instance.to_dict()
# create an instance of PeriodGetAutocompleteV2Response from a dict
period_get_autocomplete_v2_response_from_dict = PeriodGetAutocompleteV2Response.from_dict(period_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


