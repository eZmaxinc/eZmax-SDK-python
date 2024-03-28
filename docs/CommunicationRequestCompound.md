# CommunicationRequestCompound

Request for POST /1/object/communication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_communication_id** | **int** | The unique ID of the Communication. | [optional] 
**e_communication_importance** | [**FieldECommunicationImportance**](FieldECommunicationImportance.md) |  | [optional] 
**e_communication_type** | [**FieldECommunicationType**](FieldECommunicationType.md) |  | 
**obj_communicationsender** | [**CustomCommunicationsenderRequest**](CustomCommunicationsenderRequest.md) |  | [optional] 
**s_communication_subject** | **str** | The subject of the Communication | [optional] 
**t_communication_body** | **str** | The Body of the Communication | 
**b_communication_private** | **bool** | Whether the Communication is private or not | 
**e_communication_attachmenttype** | **str** | How the attachment should be included in the email.   Only used if eCommunicationType is **Email** | [optional] 
**i_communication_attachmentlinkexpiration** | **int** | The number of days before the attachment link expired.   Only used if eCommunicationType is **Email** and eCommunicationattachmentType is **Link** | [optional] 
**b_communication_readreceipt** | **bool** | Whether we ask for a read receipt or not. | [optional] 
**a_obj_communicationattachment** | [**List[CustomCommunicationattachmentRequest]**](CustomCommunicationattachmentRequest.md) |  | 
**a_obj_communicationrecipient** | [**List[CommunicationrecipientRequestCompound]**](CommunicationrecipientRequestCompound.md) |  | 
**a_obj_communicationreference** | [**List[CommunicationreferenceRequestCompound]**](CommunicationreferenceRequestCompound.md) |  | 
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
communication_request_compound_form_dict = communication_request_compound.from_dict(communication_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


