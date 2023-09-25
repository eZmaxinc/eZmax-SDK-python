# CommunicationrecipientResponseCompound

A Communicationreciient Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_communicationrecipient_id** | **int** | The unique ID of the Communicationrecipient. | 
**e_communicationrecipient_objecttype** | [**FieldECommunicationrecipientObjecttype**](FieldECommunicationrecipientObjecttype.md) |  | [optional] 
**fki_agent_id** | **int** | The unique ID of the Agent. | [optional] 
**fki_broker_id** | **int** | The unique ID of the Broker. | [optional] 
**fki_contact_id** | **int** | The unique ID of the Contact | [optional] 
**fki_customer_id** | **int** | The unique ID of the Customer. | [optional] 
**fki_employee_id** | **int** | The unique ID of the Employee. | [optional] 
**fki_ezsignsigner_id** | **int** | The unique ID of the Ezsignsigner | [optional] 
**fki_franchiseoffice_id** | **int** | The unique ID of the Franchisereoffice | [optional] 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_agentincorporation_id** | **int** | The unique ID of the Agentincorporation. | [optional] 
**fki_assistant_id** | **int** | The unique ID of the Assistant. | [optional] 
**fki_externalbroker_id** | **int** | The unique ID of the Externalbroker. | [optional] 
**fki_ezcomagent_id** | **int** | The unique ID of the Ezcomagent. | [optional] 
**fki_notary_id** | **int** | The unique ID of the Notary. | [optional] 
**fki_rewardmember_id** | **int** | The unique ID of the Rewardmember. | [optional] 
**fki_supplier_id** | **int** | The unique ID of the Supplier. | [optional] 
**e_communicationrecipient_type** | [**FieldECommunicationrecipientType**](FieldECommunicationrecipientType.md) |  | 
**obj_descriptionstatic** | [**DescriptionstaticResponseCompound**](DescriptionstaticResponseCompound.md) |  | 
**obj_emailstatic** | [**EmailstaticResponseCompound**](EmailstaticResponseCompound.md) |  | [optional] 
**obj_phonestatic** | [**PhonestaticResponseCompound**](PhonestaticResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.communicationrecipient_response_compound import CommunicationrecipientResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationrecipientResponseCompound from a JSON string
communicationrecipient_response_compound_instance = CommunicationrecipientResponseCompound.from_json(json)
# print the JSON string representation of the object
print CommunicationrecipientResponseCompound.to_json()

# convert the object into a dict
communicationrecipient_response_compound_dict = communicationrecipient_response_compound_instance.to_dict()
# create an instance of CommunicationrecipientResponseCompound from a dict
communicationrecipient_response_compound_form_dict = communicationrecipient_response_compound.from_dict(communicationrecipient_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


