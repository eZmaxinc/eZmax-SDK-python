# CommunicationattachmentResponseCompound

A Communicationattachment Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_communicationattachment_id** | **int** | The unique ID of the Communicationattachment | 
**fki_attachment_id** | **int** | The unique ID of the Attachment. | [optional] 
**fki_invoice_id** | **int** | The unique ID of the Invoice. | [optional] 
**fki_salarypreparation_id** | **int** | The unique ID of the Salarypreparation. | [optional] 
**s_communicationattachment_name** | **str** | The name of the Communicationattachment | 
**s_download_url** | **str** | The Url to the requested document.  Url will expire after 3 hours. | [optional] 

## Example

```python
from eZmaxApi.models.communicationattachment_response_compound import CommunicationattachmentResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationattachmentResponseCompound from a JSON string
communicationattachment_response_compound_instance = CommunicationattachmentResponseCompound.from_json(json)
# print the JSON string representation of the object
print CommunicationattachmentResponseCompound.to_json()

# convert the object into a dict
communicationattachment_response_compound_dict = communicationattachment_response_compound_instance.to_dict()
# create an instance of CommunicationattachmentResponseCompound from a dict
communicationattachment_response_compound_form_dict = communicationattachment_response_compound.from_dict(communicationattachment_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


