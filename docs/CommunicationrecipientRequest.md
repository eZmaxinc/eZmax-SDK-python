# CommunicationrecipientRequest

A Communicationrecipient Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_communicationrecipient_id** | **int** | The unique ID of the Communicationrecipient. | [optional] 
**fki_agent_id** | **int** | The unique ID of the Agent. | [optional] 
**fki_broker_id** | **int** | The unique ID of the Broker. | [optional] 
**fki_contact_id** | **int** | The unique ID of the Contact | [optional] 
**fki_customer_id** | **int** | The unique ID of the Customer. | [optional] 
**fki_employee_id** | **int** | The unique ID of the Employee. | [optional] 
**fki_assistant_id** | **int** | The unique ID of the Assistant. | [optional] 
**fki_externalbroker_id** | **int** | The unique ID of the Externalbroker. | [optional] 
**fki_ezsignsigner_id** | **int** | The unique ID of the Ezsignsigner | [optional] 
**fki_notary_id** | **int** | The unique ID of the Notary. | [optional] 
**fki_supplier_id** | **int** | The unique ID of the Supplier. | [optional] 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_mailboxshared_id** | **int** | The unique ID of the Mailboxshared | [optional] 
**fki_phonelineshared_id** | **int** | The unique ID of the Phonelineshared | [optional] 
**e_communicationrecipient_type** | [**FieldECommunicationrecipientType**](FieldECommunicationrecipientType.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.communicationrecipient_request import CommunicationrecipientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationrecipientRequest from a JSON string
communicationrecipient_request_instance = CommunicationrecipientRequest.from_json(json)
# print the JSON string representation of the object
print(CommunicationrecipientRequest.to_json())

# convert the object into a dict
communicationrecipient_request_dict = communicationrecipient_request_instance.to_dict()
# create an instance of CommunicationrecipientRequest from a dict
communicationrecipient_request_form_dict = communicationrecipient_request.from_dict(communicationrecipient_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


