# EzsignsigningreasonGetObjectV2Response

Response for GET /2/object/ezsignsigningreason/{pkiEzsignsigningreasonID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignsigningreasonGetObjectV2ResponseMPayload**](EzsignsigningreasonGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsigningreason_get_object_v2_response import EzsignsigningreasonGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsigningreasonGetObjectV2Response from a JSON string
ezsignsigningreason_get_object_v2_response_instance = EzsignsigningreasonGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsigningreasonGetObjectV2Response.to_json())

# convert the object into a dict
ezsignsigningreason_get_object_v2_response_dict = ezsignsigningreason_get_object_v2_response_instance.to_dict()
# create an instance of EzsignsigningreasonGetObjectV2Response from a dict
ezsignsigningreason_get_object_v2_response_from_dict = EzsignsigningreasonGetObjectV2Response.from_dict(ezsignsigningreason_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


