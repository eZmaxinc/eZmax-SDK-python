# CustomCommunicationsenderResponse

Generic Communicationsender Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_agent_id** | **int** | The unique ID of the Agent. | [optional] 
**fki_broker_id** | **int** | The unique ID of the Broker. | [optional] 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_mailboxshared_id** | **int** | The unique ID of the Mailboxshared | [optional] 
**fki_phonelineshared_id** | **int** | The unique ID of the Phonelineshared | [optional] 
**e_communicationsender_objecttype** | **str** |  | 
**obj_contact_name** | [**CustomContactNameResponse**](CustomContactNameResponse.md) |  | 
**obj_email** | [**EmailResponseCompound**](EmailResponseCompound.md) |  | [optional] 
**obj_phone_fax** | [**PhoneResponseCompound**](PhoneResponseCompound.md) |  | [optional] 
**obj_phone_sms** | [**PhoneResponseCompound**](PhoneResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.custom_communicationsender_response import CustomCommunicationsenderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomCommunicationsenderResponse from a JSON string
custom_communicationsender_response_instance = CustomCommunicationsenderResponse.from_json(json)
# print the JSON string representation of the object
print CustomCommunicationsenderResponse.to_json()

# convert the object into a dict
custom_communicationsender_response_dict = custom_communicationsender_response_instance.to_dict()
# create an instance of CustomCommunicationsenderResponse from a dict
custom_communicationsender_response_form_dict = custom_communicationsender_response.from_dict(custom_communicationsender_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


