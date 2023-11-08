# CommunicationexternalrecipientRequest

A Communicationexternalrecipient Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_communicationexternalrecipient_id** | **int** | The unique ID of the Communicationexternalrecipient | [optional] 
**s_email_address** | **str** | The email address. | [optional] 
**s_phone_e164** | **str** | A phone number in E.164 Format | [optional] 
**e_communicationexternalrecipient_type** | [**FieldECommunicationexternalrecipientType**](FieldECommunicationexternalrecipientType.md) |  | [optional] 
**s_communicationexternalrecipient_name** | **str** | The name of the Communicationexternalrecipient | 

## Example

```python
from eZmaxApi.models.communicationexternalrecipient_request import CommunicationexternalrecipientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationexternalrecipientRequest from a JSON string
communicationexternalrecipient_request_instance = CommunicationexternalrecipientRequest.from_json(json)
# print the JSON string representation of the object
print CommunicationexternalrecipientRequest.to_json()

# convert the object into a dict
communicationexternalrecipient_request_dict = communicationexternalrecipient_request_instance.to_dict()
# create an instance of CommunicationexternalrecipientRequest from a dict
communicationexternalrecipient_request_form_dict = communicationexternalrecipient_request.from_dict(communicationexternalrecipient_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


