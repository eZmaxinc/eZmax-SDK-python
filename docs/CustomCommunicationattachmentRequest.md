# CustomCommunicationattachmentRequest

A Custom Communicationattachment Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_communicationattachment** | [**CommunicationattachmentRequestCompound**](CommunicationattachmentRequestCompound.md) |  | [optional] 
**obj_communicationexternalattachment** | [**CommonFile**](CommonFile.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.custom_communicationattachment_request import CustomCommunicationattachmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomCommunicationattachmentRequest from a JSON string
custom_communicationattachment_request_instance = CustomCommunicationattachmentRequest.from_json(json)
# print the JSON string representation of the object
print CustomCommunicationattachmentRequest.to_json()

# convert the object into a dict
custom_communicationattachment_request_dict = custom_communicationattachment_request_instance.to_dict()
# create an instance of CustomCommunicationattachmentRequest from a dict
custom_communicationattachment_request_form_dict = custom_communicationattachment_request.from_dict(custom_communicationattachment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


