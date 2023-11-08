# CommunicationattachmentRequest

A Communicationattachment Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_communicationattachment_id** | **int** | The unique ID of the Communicationattachment | [optional] 
**fki_attachment_id** | **int** | The unique ID of the Attachment. | [optional] 
**fki_invoice_id** | **int** | The unique ID of the Invoice. | [optional] 
**fki_salarypreparation_id** | **int** | The unique ID of the Salarypreparation. | [optional] 

## Example

```python
from eZmaxApi.models.communicationattachment_request import CommunicationattachmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationattachmentRequest from a JSON string
communicationattachment_request_instance = CommunicationattachmentRequest.from_json(json)
# print the JSON string representation of the object
print CommunicationattachmentRequest.to_json()

# convert the object into a dict
communicationattachment_request_dict = communicationattachment_request_instance.to_dict()
# create an instance of CommunicationattachmentRequest from a dict
communicationattachment_request_form_dict = communicationattachment_request.from_dict(communicationattachment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


