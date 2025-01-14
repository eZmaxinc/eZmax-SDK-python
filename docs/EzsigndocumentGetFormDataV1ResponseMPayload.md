# EzsigndocumentGetFormDataV1ResponseMPayload

Payload for GET /1/object/ezsigndocument/{pkiEzsigndocument}/getFormData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_form_data_document** | [**CustomFormDataDocumentResponse**](CustomFormDataDocumentResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_form_data_v1_response_m_payload import EzsigndocumentGetFormDataV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetFormDataV1ResponseMPayload from a JSON string
ezsigndocument_get_form_data_v1_response_m_payload_instance = EzsigndocumentGetFormDataV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetFormDataV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigndocument_get_form_data_v1_response_m_payload_dict = ezsigndocument_get_form_data_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigndocumentGetFormDataV1ResponseMPayload from a dict
ezsigndocument_get_form_data_v1_response_m_payload_from_dict = EzsigndocumentGetFormDataV1ResponseMPayload.from_dict(ezsigndocument_get_form_data_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


