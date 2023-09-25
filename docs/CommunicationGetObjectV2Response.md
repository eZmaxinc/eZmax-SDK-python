# CommunicationGetObjectV2Response

Response for GET /2/object/communication/{pkiCommunicationID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CommunicationGetObjectV2ResponseMPayload**](CommunicationGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.communication_get_object_v2_response import CommunicationGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationGetObjectV2Response from a JSON string
communication_get_object_v2_response_instance = CommunicationGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print CommunicationGetObjectV2Response.to_json()

# convert the object into a dict
communication_get_object_v2_response_dict = communication_get_object_v2_response_instance.to_dict()
# create an instance of CommunicationGetObjectV2Response from a dict
communication_get_object_v2_response_form_dict = communication_get_object_v2_response.from_dict(communication_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


