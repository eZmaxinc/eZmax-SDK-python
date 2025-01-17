# EzsigntemplatepublicGetFormsDataV1Response

Response for GET /1/object/ezsigntemplatepublic/{pkiEzsigntemplatepublicID}/getFormsData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsigntemplatepublicGetFormsDataV1ResponseMPayload**](EzsigntemplatepublicGetFormsDataV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_get_forms_data_v1_response import EzsigntemplatepublicGetFormsDataV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicGetFormsDataV1Response from a JSON string
ezsigntemplatepublic_get_forms_data_v1_response_instance = EzsigntemplatepublicGetFormsDataV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicGetFormsDataV1Response.to_json())

# convert the object into a dict
ezsigntemplatepublic_get_forms_data_v1_response_dict = ezsigntemplatepublic_get_forms_data_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepublicGetFormsDataV1Response from a dict
ezsigntemplatepublic_get_forms_data_v1_response_from_dict = EzsigntemplatepublicGetFormsDataV1Response.from_dict(ezsigntemplatepublic_get_forms_data_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


