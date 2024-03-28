# CommunicationexternalrecipientRequestCompound

A Communicationexternalrecipient Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_communicationexternalrecipient_id** | **int** | The unique ID of the Communicationexternalrecipient | [optional] 
**s_email_address** | **str** | The email address. | [optional] 
**s_phone_e164** | **str** | A phone number in E.164 Format | [optional] 
**e_communicationexternalrecipient_type** | [**FieldECommunicationexternalrecipientType**](FieldECommunicationexternalrecipientType.md) |  | [optional] 
**s_communicationexternalrecipient_name** | **str** | The name of the Communicationexternalrecipient | [optional] 

## Example

```python
from eZmaxApi.models.communicationexternalrecipient_request_compound import CommunicationexternalrecipientRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationexternalrecipientRequestCompound from a JSON string
communicationexternalrecipient_request_compound_instance = CommunicationexternalrecipientRequestCompound.from_json(json)
# print the JSON string representation of the object
print(CommunicationexternalrecipientRequestCompound.to_json())

# convert the object into a dict
communicationexternalrecipient_request_compound_dict = communicationexternalrecipient_request_compound_instance.to_dict()
# create an instance of CommunicationexternalrecipientRequestCompound from a dict
communicationexternalrecipient_request_compound_form_dict = communicationexternalrecipient_request_compound.from_dict(communicationexternalrecipient_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


