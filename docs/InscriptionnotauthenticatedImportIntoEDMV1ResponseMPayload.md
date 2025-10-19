# InscriptionnotauthenticatedImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_import_into_edmv1_response_m_payload import InscriptionnotauthenticatedImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedImportIntoEDMV1ResponseMPayload from a JSON string
inscriptionnotauthenticated_import_into_edmv1_response_m_payload_instance = InscriptionnotauthenticatedImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
inscriptionnotauthenticated_import_into_edmv1_response_m_payload_dict = inscriptionnotauthenticated_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of InscriptionnotauthenticatedImportIntoEDMV1ResponseMPayload from a dict
inscriptionnotauthenticated_import_into_edmv1_response_m_payload_from_dict = InscriptionnotauthenticatedImportIntoEDMV1ResponseMPayload.from_dict(inscriptionnotauthenticated_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


