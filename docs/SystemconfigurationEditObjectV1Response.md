# SystemconfigurationEditObjectV1Response

Response for PUT /1/object/systemconfiguration/{pkiSystemconfigurationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.systemconfiguration_edit_object_v1_response import SystemconfigurationEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SystemconfigurationEditObjectV1Response from a JSON string
systemconfiguration_edit_object_v1_response_instance = SystemconfigurationEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(SystemconfigurationEditObjectV1Response.to_json())

# convert the object into a dict
systemconfiguration_edit_object_v1_response_dict = systemconfiguration_edit_object_v1_response_instance.to_dict()
# create an instance of SystemconfigurationEditObjectV1Response from a dict
systemconfiguration_edit_object_v1_response_from_dict = SystemconfigurationEditObjectV1Response.from_dict(systemconfiguration_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


