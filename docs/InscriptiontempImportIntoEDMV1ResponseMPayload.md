# InscriptiontempImportIntoEDMV1ResponseMPayload

Payload for POST/1/object/inscriptiontemp/{pkiInscriptiontempID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptiontemp_import_into_edmv1_response_m_payload import InscriptiontempImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptiontempImportIntoEDMV1ResponseMPayload from a JSON string
inscriptiontemp_import_into_edmv1_response_m_payload_instance = InscriptiontempImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InscriptiontempImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
inscriptiontemp_import_into_edmv1_response_m_payload_dict = inscriptiontemp_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of InscriptiontempImportIntoEDMV1ResponseMPayload from a dict
inscriptiontemp_import_into_edmv1_response_m_payload_from_dict = InscriptiontempImportIntoEDMV1ResponseMPayload.from_dict(inscriptiontemp_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


