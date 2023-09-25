# CommunicationexternalrecipientResponse

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
from eZmaxApi.models.communicationexternalrecipient_response import CommunicationexternalrecipientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationexternalrecipientResponse from a JSON string
communicationexternalrecipient_response_instance = CommunicationexternalrecipientResponse.from_json(json)
# print the JSON string representation of the object
print CommunicationexternalrecipientResponse.to_json()

# convert the object into a dict
communicationexternalrecipient_response_dict = communicationexternalrecipient_response_instance.to_dict()
# create an instance of CommunicationexternalrecipientResponse from a dict
communicationexternalrecipient_response_form_dict = communicationexternalrecipient_response.from_dict(communicationexternalrecipient_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


