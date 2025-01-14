# DomainCreateObjectV1Request

Request for POST /1/object/domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_domain** | [**List[DomainRequestCompound]**](DomainRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.domain_create_object_v1_request import DomainCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCreateObjectV1Request from a JSON string
domain_create_object_v1_request_instance = DomainCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(DomainCreateObjectV1Request.to_json())

# convert the object into a dict
domain_create_object_v1_request_dict = domain_create_object_v1_request_instance.to_dict()
# create an instance of DomainCreateObjectV1Request from a dict
domain_create_object_v1_request_from_dict = DomainCreateObjectV1Request.from_dict(domain_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


