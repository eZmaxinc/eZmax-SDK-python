# DomainRequest

A Domain Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_domain_id** | **int** | The unique ID of the Domain | [optional] 
**s_domain_name** | **str** | The name of the Domain | 

## Example

```python
from eZmaxApi.models.domain_request import DomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainRequest from a JSON string
domain_request_instance = DomainRequest.from_json(json)
# print the JSON string representation of the object
print(DomainRequest.to_json())

# convert the object into a dict
domain_request_dict = domain_request_instance.to_dict()
# create an instance of DomainRequest from a dict
domain_request_from_dict = DomainRequest.from_dict(domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


