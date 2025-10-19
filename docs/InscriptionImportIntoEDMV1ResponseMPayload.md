# InscriptionImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/inscription/{pkiInscriptionID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.inscription_import_into_edmv1_response_m_payload import InscriptionImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionImportIntoEDMV1ResponseMPayload from a JSON string
inscription_import_into_edmv1_response_m_payload_instance = InscriptionImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InscriptionImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
inscription_import_into_edmv1_response_m_payload_dict = inscription_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of InscriptionImportIntoEDMV1ResponseMPayload from a dict
inscription_import_into_edmv1_response_m_payload_from_dict = InscriptionImportIntoEDMV1ResponseMPayload.from_dict(inscription_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


