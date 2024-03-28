# CommunicationreferenceRequestCompound

A Communicationreference Object and children

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
from eZmaxApi.models.communicationreference_request_compound import CommunicationreferenceRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationreferenceRequestCompound from a JSON string
communicationreference_request_compound_instance = CommunicationreferenceRequestCompound.from_json(json)
# print the JSON string representation of the object
print(CommunicationreferenceRequestCompound.to_json())

# convert the object into a dict
communicationreference_request_compound_dict = communicationreference_request_compound_instance.to_dict()
# create an instance of CommunicationreferenceRequestCompound from a dict
communicationreference_request_compound_form_dict = communicationreference_request_compound.from_dict(communicationreference_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


