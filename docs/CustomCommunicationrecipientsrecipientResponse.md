# CustomCommunicationrecipientsrecipientResponse

Generic AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**e_communicationrecipientsrecipient_objecttype** | **str** |  | 
**obj_contact_name** | [**CustomContactNameResponse**](CustomContactNameResponse.md) |  | 
**obj_email** | [**EmailResponse**](EmailResponse.md) | An Email Object and children to create a complete structure | [optional] 
**obj_phone_fax** | [**PhoneResponseCompound**](PhoneResponseCompound.md) |  | [optional] 
**obj_phone_sms** | [**PhoneResponseCompound**](PhoneResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.custom_communicationrecipientsrecipient_response import CustomCommunicationrecipientsrecipientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomCommunicationrecipientsrecipientResponse from a JSON string
custom_communicationrecipientsrecipient_response_instance = CustomCommunicationrecipientsrecipientResponse.from_json(json)
# print the JSON string representation of the object
print(CustomCommunicationrecipientsrecipientResponse.to_json())

# convert the object into a dict
custom_communicationrecipientsrecipient_response_dict = custom_communicationrecipientsrecipient_response_instance.to_dict()
# create an instance of CustomCommunicationrecipientsrecipientResponse from a dict
custom_communicationrecipientsrecipient_response_from_dict = CustomCommunicationrecipientsrecipientResponse.from_dict(custom_communicationrecipientsrecipient_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


