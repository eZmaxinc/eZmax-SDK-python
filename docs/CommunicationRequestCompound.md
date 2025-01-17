# CommunicationRequestCompound

Request for POST /1/object/communication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationattachment** | [**List[CustomCommunicationattachmentRequest]**](CustomCommunicationattachmentRequest.md) |  | 
**a_obj_communicationrecipient** | [**List[CommunicationrecipientRequestCompound]**](CommunicationrecipientRequestCompound.md) |  | 
**a_obj_communicationreference** | [**List[CommunicationreferenceRequestCompound]**](CommunicationreferenceRequest.md) |  | 
**a_obj_communicationexternalrecipient** | [**List[CommunicationexternalrecipientRequestCompound]**](CommunicationexternalrecipientRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.communication_request_compound import CommunicationRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationRequestCompound from a JSON string
communication_request_compound_instance = CommunicationRequestCompound.from_json(json)
# print the JSON string representation of the object
print(CommunicationRequestCompound.to_json())

# convert the object into a dict
communication_request_compound_dict = communication_request_compound_instance.to_dict()
# create an instance of CommunicationRequestCompound from a dict
communication_request_compound_from_dict = CommunicationRequestCompound.from_dict(communication_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


