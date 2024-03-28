# EzsignbulksendGetFormsDataV1ResponseMPayload

Payload for GET/1/object/ezsignbulksend/{pkiEzsignbulksendID}/getFormsData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_forms_data_folder** | [**List[CustomFormsDataFolderResponse]**](CustomFormsDataFolderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_get_forms_data_v1_response_m_payload import EzsignbulksendGetFormsDataV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendGetFormsDataV1ResponseMPayload from a JSON string
ezsignbulksend_get_forms_data_v1_response_m_payload_instance = EzsignbulksendGetFormsDataV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendGetFormsDataV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignbulksend_get_forms_data_v1_response_m_payload_dict = ezsignbulksend_get_forms_data_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignbulksendGetFormsDataV1ResponseMPayload from a dict
ezsignbulksend_get_forms_data_v1_response_m_payload_form_dict = ezsignbulksend_get_forms_data_v1_response_m_payload.from_dict(ezsignbulksend_get_forms_data_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


