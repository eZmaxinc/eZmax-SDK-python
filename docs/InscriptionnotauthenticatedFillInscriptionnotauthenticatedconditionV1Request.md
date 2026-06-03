# InscriptionnotauthenticatedFillInscriptionnotauthenticatedconditionV1Request

Request for POST /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/fillInscriptionnotauthenticatedcondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_inscriptionnotauthenticatedcondition** | [**List[CustomInscriptionnotauthenticatedconditionRequest]**](CustomInscriptionnotauthenticatedconditionRequest.md) |  | 
**dt_inscriptionnotauthenticated_transactiondate_real** | **str** | The transactiondatereal of the Inscriptionnotauthenticated | [optional] 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_fill_inscriptionnotauthenticatedcondition_v1_request import InscriptionnotauthenticatedFillInscriptionnotauthenticatedconditionV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedFillInscriptionnotauthenticatedconditionV1Request from a JSON string
inscriptionnotauthenticated_fill_inscriptionnotauthenticatedcondition_v1_request_instance = InscriptionnotauthenticatedFillInscriptionnotauthenticatedconditionV1Request.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedFillInscriptionnotauthenticatedconditionV1Request.to_json())

# convert the object into a dict
inscriptionnotauthenticated_fill_inscriptionnotauthenticatedcondition_v1_request_dict = inscriptionnotauthenticated_fill_inscriptionnotauthenticatedcondition_v1_request_instance.to_dict()
# create an instance of InscriptionnotauthenticatedFillInscriptionnotauthenticatedconditionV1Request from a dict
inscriptionnotauthenticated_fill_inscriptionnotauthenticatedcondition_v1_request_from_dict = InscriptionnotauthenticatedFillInscriptionnotauthenticatedconditionV1Request.from_dict(inscriptionnotauthenticated_fill_inscriptionnotauthenticatedcondition_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


