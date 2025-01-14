# DomainRequestCompound

A Domain Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_domain_id** | **int** | The unique ID of the Domain | [optional] 
**s_domain_name** | **str** | The name of the Domain | 

## Example

```python
from eZmaxApi.models.domain_request_compound import DomainRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of DomainRequestCompound from a JSON string
domain_request_compound_instance = DomainRequestCompound.from_json(json)
# print the JSON string representation of the object
print(DomainRequestCompound.to_json())

# convert the object into a dict
domain_request_compound_dict = domain_request_compound_instance.to_dict()
# create an instance of DomainRequestCompound from a dict
domain_request_compound_from_dict = DomainRequestCompound.from_dict(domain_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


