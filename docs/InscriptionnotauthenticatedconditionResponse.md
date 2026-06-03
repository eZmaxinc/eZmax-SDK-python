# InscriptionnotauthenticatedconditionResponse

An Inscriptionnotauthenticatedcondition Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_inscriptionnotauthenticatedcondition_id** | **int** | The unique ID of the Inscriptionnotauthenticatedcondition | 
**fki_inscriptionnotauthenticatedconditiontype_id** | **int** | The unique ID of the Inscriptionnotauthenticatedconditiontype | 
**s_inscriptionnotauthenticatedconditiontype_name_x** | **str** | The name of the Inscriptionnotauthenticatedconditiontype in the language of the requester | 
**fki_inscriptionnotauthenticated_id** | **int** | The unique ID of the Inscriptionnotauthenticated. | 
**b_inscriptionnotauthenticatedcondition_filled** | **bool** | Can access attachment when we clone a user | 
**dt_inscriptionnotauthenticatedcondition_completed** | **str** | The date the Inscriptionnotauthenticatedcondition was completed | [optional] 
**dt_inscriptionnotauthenticatedcondition_due** | **str** | The date the Inscriptionnotauthenticatedcondition is due | [optional] 
**t_inscriptionnotauthenticatedcondition_comment** | **str** | The comment of the Inscriptionnotauthenticatedcondition | 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticatedcondition_response import InscriptionnotauthenticatedconditionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedconditionResponse from a JSON string
inscriptionnotauthenticatedcondition_response_instance = InscriptionnotauthenticatedconditionResponse.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedconditionResponse.to_json())

# convert the object into a dict
inscriptionnotauthenticatedcondition_response_dict = inscriptionnotauthenticatedcondition_response_instance.to_dict()
# create an instance of InscriptionnotauthenticatedconditionResponse from a dict
inscriptionnotauthenticatedcondition_response_from_dict = InscriptionnotauthenticatedconditionResponse.from_dict(inscriptionnotauthenticatedcondition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


