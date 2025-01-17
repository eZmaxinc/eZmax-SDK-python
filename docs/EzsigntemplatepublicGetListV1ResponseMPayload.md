# EzsigntemplatepublicGetListV1ResponseMPayload

Payload for GET /1/object/ezsigntemplatepublic/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatepublic** | [**List[EzsigntemplatepublicListElement]**](EzsigntemplatepublicListElement.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_get_list_v1_response_m_payload import EzsigntemplatepublicGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicGetListV1ResponseMPayload from a JSON string
ezsigntemplatepublic_get_list_v1_response_m_payload_instance = EzsigntemplatepublicGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicGetListV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatepublic_get_list_v1_response_m_payload_dict = ezsigntemplatepublic_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepublicGetListV1ResponseMPayload from a dict
ezsigntemplatepublic_get_list_v1_response_m_payload_from_dict = EzsigntemplatepublicGetListV1ResponseMPayload.from_dict(ezsigntemplatepublic_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


