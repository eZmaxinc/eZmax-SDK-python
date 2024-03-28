# EzsignfolderGetFormsDataV1ResponseMPayload

Payload for GET /1/object/ezsignfolder/{pkiEzsigndocument}/getFormsData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_forms_data_folder** | [**CustomFormsDataFolderResponse**](CustomFormsDataFolderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_forms_data_v1_response_m_payload import EzsignfolderGetFormsDataV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetFormsDataV1ResponseMPayload from a JSON string
ezsignfolder_get_forms_data_v1_response_m_payload_instance = EzsignfolderGetFormsDataV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetFormsDataV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignfolder_get_forms_data_v1_response_m_payload_dict = ezsignfolder_get_forms_data_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderGetFormsDataV1ResponseMPayload from a dict
ezsignfolder_get_forms_data_v1_response_m_payload_form_dict = ezsignfolder_get_forms_data_v1_response_m_payload.from_dict(ezsignfolder_get_forms_data_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


