# DomainCreateObjectV1Response

Response for POST /1/object/domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**DomainCreateObjectV1ResponseMPayload**](DomainCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.domain_create_object_v1_response import DomainCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCreateObjectV1Response from a JSON string
domain_create_object_v1_response_instance = DomainCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(DomainCreateObjectV1Response.to_json())

# convert the object into a dict
domain_create_object_v1_response_dict = domain_create_object_v1_response_instance.to_dict()
# create an instance of DomainCreateObjectV1Response from a dict
domain_create_object_v1_response_from_dict = DomainCreateObjectV1Response.from_dict(domain_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


