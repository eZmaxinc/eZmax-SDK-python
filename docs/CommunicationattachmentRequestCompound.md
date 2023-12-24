# CommunicationattachmentRequestCompound

A Communicationattachment Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_communicationattachment_id** | **int** | The unique ID of the Communicationattachment | [optional] 
**fki_attachment_id** | **int** | The unique ID of the Attachment. | [optional] 
**fki_invoice_id** | **int** | The unique ID of the Invoice. | [optional] 
**fki_salarypreparation_id** | **int** | The unique ID of the Salarypreparation. | [optional] 

## Example

```python
from eZmaxApi.models.communicationattachment_request_compound import CommunicationattachmentRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationattachmentRequestCompound from a JSON string
communicationattachment_request_compound_instance = CommunicationattachmentRequestCompound.from_json(json)
# print the JSON string representation of the object
print CommunicationattachmentRequestCompound.to_json()

# convert the object into a dict
communicationattachment_request_compound_dict = communicationattachment_request_compound_instance.to_dict()
# create an instance of CommunicationattachmentRequestCompound from a dict
communicationattachment_request_compound_form_dict = communicationattachment_request_compound.from_dict(communicationattachment_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


