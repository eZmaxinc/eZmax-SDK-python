# CommunicationResponseCompound

A Communication Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_communication_id** | **int** | The unique ID of the Communication. | 
**e_communication_importance** | [**FieldECommunicationImportance**](FieldECommunicationImportance.md) |  | 
**e_communication_type** | [**FieldECommunicationType**](FieldECommunicationType.md) |  | 
**s_communication_subject** | **str** | The subject of the Communication | 
**s_communication_bodyurl** | **str** | The url of the body used as body in the Communication | [optional] 
**e_communication_direction** | [**ComputedECommunicationDirection**](ComputedECommunicationDirection.md) |  | 
**i_communicationrecipient_count** | **int** | The count of Communicationrecipient | 
**b_communication_private** | **bool** | Whether the Communication is private or not | 
**obj_descriptionstatic_sender** | [**DescriptionstaticResponse**](DescriptionstaticResponse.md) |  | [optional] 
**obj_emailstatic_sender** | [**EmailstaticResponse**](EmailstaticResponse.md) |  | [optional] 
**obj_phonestatic_sender** | [**PhonestaticResponse**](PhonestaticResponse.md) |  | [optional] 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 
**a_obj_communicationattachment** | [**List[CommunicationattachmentResponseCompound]**](CommunicationattachmentResponseCompound.md) |  | 
**a_obj_communicationrecipient** | [**List[CommunicationrecipientResponseCompound]**](CommunicationrecipientResponseCompound.md) |  | 
**a_obj_communicationexternalrecipient** | [**List[CommunicationexternalrecipientResponseCompound]**](CommunicationexternalrecipientResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.communication_response_compound import CommunicationResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationResponseCompound from a JSON string
communication_response_compound_instance = CommunicationResponseCompound.from_json(json)
# print the JSON string representation of the object
print CommunicationResponseCompound.to_json()

# convert the object into a dict
communication_response_compound_dict = communication_response_compound_instance.to_dict()
# create an instance of CommunicationResponseCompound from a dict
communication_response_compound_form_dict = communication_response_compound.from_dict(communication_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


