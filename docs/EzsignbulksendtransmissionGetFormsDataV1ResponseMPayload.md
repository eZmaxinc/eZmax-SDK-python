# EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload

Payload for GET /1/object/ezsignbulksendtransmission/{pkiEzsignbulksendtransmissionID}/getFormsData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_forms_data_folder** | [**List[CustomFormsDataFolderResponse]**](CustomFormsDataFolderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendtransmission_get_forms_data_v1_response_m_payload import EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload from a JSON string
ezsignbulksendtransmission_get_forms_data_v1_response_m_payload_instance = EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignbulksendtransmission_get_forms_data_v1_response_m_payload_dict = ezsignbulksendtransmission_get_forms_data_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload from a dict
ezsignbulksendtransmission_get_forms_data_v1_response_m_payload_from_dict = EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload.from_dict(ezsignbulksendtransmission_get_forms_data_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


