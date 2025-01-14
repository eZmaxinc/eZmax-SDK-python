# SystemconfigurationGetObjectV2Response

Response for GET /2/object/systemconfiguration/{pkiSystemconfigurationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SystemconfigurationGetObjectV2ResponseMPayload**](SystemconfigurationGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.systemconfiguration_get_object_v2_response import SystemconfigurationGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of SystemconfigurationGetObjectV2Response from a JSON string
systemconfiguration_get_object_v2_response_instance = SystemconfigurationGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(SystemconfigurationGetObjectV2Response.to_json())

# convert the object into a dict
systemconfiguration_get_object_v2_response_dict = systemconfiguration_get_object_v2_response_instance.to_dict()
# create an instance of SystemconfigurationGetObjectV2Response from a dict
systemconfiguration_get_object_v2_response_from_dict = SystemconfigurationGetObjectV2Response.from_dict(systemconfiguration_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


