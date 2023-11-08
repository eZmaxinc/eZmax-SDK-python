# CustomCommunicationrecipientsgroupResponse

Generic CommunicationrecipientsGroup Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_communicationrecipientsgroup_label** | **str** | The label for the Communicationrecipientsgroup | 
**a_obj_communicationrecipientsrecipient** | [**List[CustomCommunicationrecipientsrecipientResponse]**](CustomCommunicationrecipientsrecipientResponse.md) |  | 

## Example

```python
from eZmaxApi.models.custom_communicationrecipientsgroup_response import CustomCommunicationrecipientsgroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomCommunicationrecipientsgroupResponse from a JSON string
custom_communicationrecipientsgroup_response_instance = CustomCommunicationrecipientsgroupResponse.from_json(json)
# print the JSON string representation of the object
print CustomCommunicationrecipientsgroupResponse.to_json()

# convert the object into a dict
custom_communicationrecipientsgroup_response_dict = custom_communicationrecipientsgroup_response_instance.to_dict()
# create an instance of CustomCommunicationrecipientsgroupResponse from a dict
custom_communicationrecipientsgroup_response_form_dict = custom_communicationrecipientsgroup_response.from_dict(custom_communicationrecipientsgroup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


