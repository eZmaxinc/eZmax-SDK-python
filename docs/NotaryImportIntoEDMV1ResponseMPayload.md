# NotaryImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/notary/{pkiNotaryID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.notary_import_into_edmv1_response_m_payload import NotaryImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of NotaryImportIntoEDMV1ResponseMPayload from a JSON string
notary_import_into_edmv1_response_m_payload_instance = NotaryImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(NotaryImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
notary_import_into_edmv1_response_m_payload_dict = notary_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of NotaryImportIntoEDMV1ResponseMPayload from a dict
notary_import_into_edmv1_response_m_payload_from_dict = NotaryImportIntoEDMV1ResponseMPayload.from_dict(notary_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


