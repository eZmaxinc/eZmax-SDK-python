# ActivesessionGetCurrentV1Response

Response for GET /1/object/activesession/getCurrent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ActivesessionGetCurrentV1ResponseMPayload**](ActivesessionGetCurrentV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.activesession_get_current_v1_response import ActivesessionGetCurrentV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActivesessionGetCurrentV1Response from a JSON string
activesession_get_current_v1_response_instance = ActivesessionGetCurrentV1Response.from_json(json)
# print the JSON string representation of the object
print ActivesessionGetCurrentV1Response.to_json()

# convert the object into a dict
activesession_get_current_v1_response_dict = activesession_get_current_v1_response_instance.to_dict()
# create an instance of ActivesessionGetCurrentV1Response from a dict
activesession_get_current_v1_response_form_dict = activesession_get_current_v1_response.from_dict(activesession_get_current_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


