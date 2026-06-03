# CustomInscriptionnotauthenticatedconditionRequest

A custom Inscriptionnotauthenticatedcondition object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_inscriptionnotauthenticatedcondition_id** | **int** | The unique ID of the Inscriptionnotauthenticatedcondition | 
**dt_inscriptionnotauthenticatedcondition_completed** | **str** | The date the Inscriptionnotauthenticatedcondition was completed | 

## Example

```python
from eZmaxApi.models.custom_inscriptionnotauthenticatedcondition_request import CustomInscriptionnotauthenticatedconditionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInscriptionnotauthenticatedconditionRequest from a JSON string
custom_inscriptionnotauthenticatedcondition_request_instance = CustomInscriptionnotauthenticatedconditionRequest.from_json(json)
# print the JSON string representation of the object
print(CustomInscriptionnotauthenticatedconditionRequest.to_json())

# convert the object into a dict
custom_inscriptionnotauthenticatedcondition_request_dict = custom_inscriptionnotauthenticatedcondition_request_instance.to_dict()
# create an instance of CustomInscriptionnotauthenticatedconditionRequest from a dict
custom_inscriptionnotauthenticatedcondition_request_from_dict = CustomInscriptionnotauthenticatedconditionRequest.from_dict(custom_inscriptionnotauthenticatedcondition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


