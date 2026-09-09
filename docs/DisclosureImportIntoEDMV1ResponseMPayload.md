# DisclosureImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/disclosure/{pkiDisclosureID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.disclosure_import_into_edmv1_response_m_payload import DisclosureImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureImportIntoEDMV1ResponseMPayload from a JSON string
disclosure_import_into_edmv1_response_m_payload_instance = DisclosureImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DisclosureImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
disclosure_import_into_edmv1_response_m_payload_dict = disclosure_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of DisclosureImportIntoEDMV1ResponseMPayload from a dict
disclosure_import_into_edmv1_response_m_payload_from_dict = DisclosureImportIntoEDMV1ResponseMPayload.from_dict(disclosure_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


