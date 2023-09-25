# CommunicationexternalrecipientResponseCompound

A Communicationexternalrecipient Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_communicationexternalrecipient_id** | **int** | The unique ID of the Communicationexternalrecipient | 
**e_communicationexternalrecipient_type** | [**FieldECommunicationexternalrecipientType**](FieldECommunicationexternalrecipientType.md) |  | 
**obj_descriptionstatic** | [**DescriptionstaticResponseCompound**](DescriptionstaticResponseCompound.md) |  | 
**obj_emailstatic** | [**EmailstaticResponseCompound**](EmailstaticResponseCompound.md) |  | [optional] 
**obj_phonestatic** | [**PhonestaticResponseCompound**](PhonestaticResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.communicationexternalrecipient_response_compound import CommunicationexternalrecipientResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationexternalrecipientResponseCompound from a JSON string
communicationexternalrecipient_response_compound_instance = CommunicationexternalrecipientResponseCompound.from_json(json)
# print the JSON string representation of the object
print CommunicationexternalrecipientResponseCompound.to_json()

# convert the object into a dict
communicationexternalrecipient_response_compound_dict = communicationexternalrecipient_response_compound_instance.to_dict()
# create an instance of CommunicationexternalrecipientResponseCompound from a dict
communicationexternalrecipient_response_compound_form_dict = communicationexternalrecipient_response_compound.from_dict(communicationexternalrecipient_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


