# EzsignsigningreasonCreateObjectV1Response

Response for POST /1/object/ezsignsigningreason

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignsigningreasonCreateObjectV1ResponseMPayload**](EzsignsigningreasonCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsigningreason_create_object_v1_response import EzsignsigningreasonCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsigningreasonCreateObjectV1Response from a JSON string
ezsignsigningreason_create_object_v1_response_instance = EzsignsigningreasonCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsigningreasonCreateObjectV1Response.to_json())

# convert the object into a dict
ezsignsigningreason_create_object_v1_response_dict = ezsignsigningreason_create_object_v1_response_instance.to_dict()
# create an instance of EzsignsigningreasonCreateObjectV1Response from a dict
ezsignsigningreason_create_object_v1_response_form_dict = ezsignsigningreason_create_object_v1_response.from_dict(ezsignsigningreason_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


