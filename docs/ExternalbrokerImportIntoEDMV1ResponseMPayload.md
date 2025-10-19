# ExternalbrokerImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/externalbroker/{pkiExternalbrokerID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.externalbroker_import_into_edmv1_response_m_payload import ExternalbrokerImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalbrokerImportIntoEDMV1ResponseMPayload from a JSON string
externalbroker_import_into_edmv1_response_m_payload_instance = ExternalbrokerImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ExternalbrokerImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
externalbroker_import_into_edmv1_response_m_payload_dict = externalbroker_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of ExternalbrokerImportIntoEDMV1ResponseMPayload from a dict
externalbroker_import_into_edmv1_response_m_payload_from_dict = ExternalbrokerImportIntoEDMV1ResponseMPayload.from_dict(externalbroker_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


