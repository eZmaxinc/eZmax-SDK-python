# EzsignfoldersignerassociationResponse

An Ezsignfoldersignerassociation Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | 
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**b_ezsignfoldersignerassociation_delayedsend** | **bool** | If this flag is true the signatory is part of a delayed send. | 
**b_ezsignfoldersignerassociation_receivecopy** | **bool** | If this flag is true. The signatory will receive a copy of every signed Ezsigndocument even if it ain&#39;t required to sign the document. | 
**t_ezsignfoldersignerassociation_message** | **str** | A custom text message that will be added to the email sent. | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_response import EzsignfoldersignerassociationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationResponse from a JSON string
ezsignfoldersignerassociation_response_instance = EzsignfoldersignerassociationResponse.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationResponse.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_response_dict = ezsignfoldersignerassociation_response_instance.to_dict()
# create an instance of EzsignfoldersignerassociationResponse from a dict
ezsignfoldersignerassociation_response_form_dict = ezsignfoldersignerassociation_response.from_dict(ezsignfoldersignerassociation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


