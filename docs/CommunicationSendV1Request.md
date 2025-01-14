# CommunicationSendV1Request

Request for POST /1/object/communication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communication** | [**List[CommunicationRequestCompound]**](CommunicationRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.communication_send_v1_request import CommunicationSendV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationSendV1Request from a JSON string
communication_send_v1_request_instance = CommunicationSendV1Request.from_json(json)
# print the JSON string representation of the object
print(CommunicationSendV1Request.to_json())

# convert the object into a dict
communication_send_v1_request_dict = communication_send_v1_request_instance.to_dict()
# create an instance of CommunicationSendV1Request from a dict
communication_send_v1_request_from_dict = CommunicationSendV1Request.from_dict(communication_send_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


