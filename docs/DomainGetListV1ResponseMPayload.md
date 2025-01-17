# DomainGetListV1ResponseMPayload

Payload for GET /1/object/domain/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_domain** | [**List[DomainListElement]**](DomainListElement.md) |  | 

## Example

```python
from eZmaxApi.models.domain_get_list_v1_response_m_payload import DomainGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DomainGetListV1ResponseMPayload from a JSON string
domain_get_list_v1_response_m_payload_instance = DomainGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DomainGetListV1ResponseMPayload.to_json())

# convert the object into a dict
domain_get_list_v1_response_m_payload_dict = domain_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of DomainGetListV1ResponseMPayload from a dict
domain_get_list_v1_response_m_payload_from_dict = DomainGetListV1ResponseMPayload.from_dict(domain_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


