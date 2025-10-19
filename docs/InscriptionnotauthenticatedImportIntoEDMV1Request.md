# InscriptionnotauthenticatedImportIntoEDMV1Request

Request for POST /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_import_into_edmv1_request import InscriptionnotauthenticatedImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedImportIntoEDMV1Request from a JSON string
inscriptionnotauthenticated_import_into_edmv1_request_instance = InscriptionnotauthenticatedImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedImportIntoEDMV1Request.to_json())

# convert the object into a dict
inscriptionnotauthenticated_import_into_edmv1_request_dict = inscriptionnotauthenticated_import_into_edmv1_request_instance.to_dict()
# create an instance of InscriptionnotauthenticatedImportIntoEDMV1Request from a dict
inscriptionnotauthenticated_import_into_edmv1_request_from_dict = InscriptionnotauthenticatedImportIntoEDMV1Request.from_dict(inscriptionnotauthenticated_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


