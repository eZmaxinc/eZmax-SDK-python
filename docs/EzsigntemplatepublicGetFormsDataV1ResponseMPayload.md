# EzsigntemplatepublicGetFormsDataV1ResponseMPayload

Payload for GET/1/object/ezsigntemplatepublic/{pkiEzsigntemplatepublicID}/getFormsData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_forms_data_folder** | [**List[CustomFormsDataFolderResponse]**](CustomFormsDataFolderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_get_forms_data_v1_response_m_payload import EzsigntemplatepublicGetFormsDataV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicGetFormsDataV1ResponseMPayload from a JSON string
ezsigntemplatepublic_get_forms_data_v1_response_m_payload_instance = EzsigntemplatepublicGetFormsDataV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicGetFormsDataV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatepublic_get_forms_data_v1_response_m_payload_dict = ezsigntemplatepublic_get_forms_data_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepublicGetFormsDataV1ResponseMPayload from a dict
ezsigntemplatepublic_get_forms_data_v1_response_m_payload_from_dict = EzsigntemplatepublicGetFormsDataV1ResponseMPayload.from_dict(ezsigntemplatepublic_get_forms_data_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


