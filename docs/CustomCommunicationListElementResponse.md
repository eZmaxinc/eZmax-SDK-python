# CustomCommunicationListElementResponse

A Communication List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_communication_id** | **int** | The unique ID of the Communication. | 
**dt_created_date** | **str** | The date and time at which the object was created | 
**e_communication_direction** | [**ComputedECommunicationDirection**](ComputedECommunicationDirection.md) |  | 
**e_communication_importance** | [**FieldECommunicationImportance**](FieldECommunicationImportance.md) |  | 
**e_communication_type** | [**FieldECommunicationType**](FieldECommunicationType.md) |  | 
**i_communicationrecipient_count** | **int** | The count of Communicationrecipient | 
**s_communication_subject** | **str** | The subject of the Communication | 
**s_communication_sender** | **str** | The sender name of the Communication | 
**s_communication_recipient** | **str** | The recipients&#39; name of the Communication | 

## Example

```python
from eZmaxApi.models.custom_communication_list_element_response import CustomCommunicationListElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomCommunicationListElementResponse from a JSON string
custom_communication_list_element_response_instance = CustomCommunicationListElementResponse.from_json(json)
# print the JSON string representation of the object
print CustomCommunicationListElementResponse.to_json()

# convert the object into a dict
custom_communication_list_element_response_dict = custom_communication_list_element_response_instance.to_dict()
# create an instance of CustomCommunicationListElementResponse from a dict
custom_communication_list_element_response_form_dict = custom_communication_list_element_response.from_dict(custom_communication_list_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


