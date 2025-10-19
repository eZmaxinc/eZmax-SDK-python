# OtherincomeImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/otherincome/{pkiOtherincomeID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.otherincome_import_into_edmv1_response_m_payload import OtherincomeImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of OtherincomeImportIntoEDMV1ResponseMPayload from a JSON string
otherincome_import_into_edmv1_response_m_payload_instance = OtherincomeImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(OtherincomeImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
otherincome_import_into_edmv1_response_m_payload_dict = otherincome_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of OtherincomeImportIntoEDMV1ResponseMPayload from a dict
otherincome_import_into_edmv1_response_m_payload_from_dict = OtherincomeImportIntoEDMV1ResponseMPayload.from_dict(otherincome_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


