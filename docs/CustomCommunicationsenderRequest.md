# CustomCommunicationsenderRequest

A Communicationsender Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_agent_id** | **int** | The unique ID of the Agent. | [optional] 
**fki_broker_id** | **int** | The unique ID of the Broker. | [optional] 
**fki_mailboxshared_id** | **int** | The unique ID of the Mailboxshared | [optional] 
**fki_phonelineshared_id** | **int** | The unique ID of the Phonelineshared | [optional] 
**fki_user_id** | **int** | The unique ID of the User | [optional] 

## Example

```python
from eZmaxApi.models.custom_communicationsender_request import CustomCommunicationsenderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomCommunicationsenderRequest from a JSON string
custom_communicationsender_request_instance = CustomCommunicationsenderRequest.from_json(json)
# print the JSON string representation of the object
print(CustomCommunicationsenderRequest.to_json())

# convert the object into a dict
custom_communicationsender_request_dict = custom_communicationsender_request_instance.to_dict()
# create an instance of CustomCommunicationsenderRequest from a dict
custom_communicationsender_request_from_dict = CustomCommunicationsenderRequest.from_dict(custom_communicationsender_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


