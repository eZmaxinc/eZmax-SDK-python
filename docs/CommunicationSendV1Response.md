# CommunicationSendV1Response

Response for POST /1/object/communication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CommunicationCreateObjectV1ResponseMPayload**](CommunicationCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.communication_send_v1_response import CommunicationSendV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationSendV1Response from a JSON string
communication_send_v1_response_instance = CommunicationSendV1Response.from_json(json)
# print the JSON string representation of the object
print(CommunicationSendV1Response.to_json())

# convert the object into a dict
communication_send_v1_response_dict = communication_send_v1_response_instance.to_dict()
# create an instance of CommunicationSendV1Response from a dict
communication_send_v1_response_form_dict = communication_send_v1_response.from_dict(communication_send_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


