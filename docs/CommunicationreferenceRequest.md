# CommunicationreferenceRequest

A Communicationreference Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_communicationreference_id** | **int** | The unique ID of the Communicationreference | [optional] 
**fki_buyercontract_id** | **int** | The unique ID of the Buyercontract | [optional] 
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | [optional] 
**fki_inscription_id** | **int** | The unique ID of the Inscription. | [optional] 
**fki_inscriptiontemp_id** | **int** | The unique ID of the Inscriptiontemp | [optional] 
**fki_invoice_id** | **int** | The unique ID of the Invoice. | [optional] 
**fki_otherincome_id** | **int** | The unique ID of the Otherincome | [optional] 
**fki_electronicfundstransfer_id** | **int** | The unique ID of the Electronicfundstransfer | [optional] 
**fki_rejectedoffertopurchase_id** | **int** | The unique ID of the Rejectedoffertopurchase | [optional] 

## Example

```python
from eZmaxApi.models.communicationreference_request import CommunicationreferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationreferenceRequest from a JSON string
communicationreference_request_instance = CommunicationreferenceRequest.from_json(json)
# print the JSON string representation of the object
print CommunicationreferenceRequest.to_json()

# convert the object into a dict
communicationreference_request_dict = communicationreference_request_instance.to_dict()
# create an instance of CommunicationreferenceRequest from a dict
communicationreference_request_form_dict = communicationreference_request.from_dict(communicationreference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


