# DomainResponseCompound

A Domain Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_dnsrecord** | **List[CustomDnsrecordResponse]** |  | 

## Example

```python
from eZmaxApi.models.domain_response_compound import DomainResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of DomainResponseCompound from a JSON string
domain_response_compound_instance = DomainResponseCompound.from_json(json)
# print the JSON string representation of the object
print(DomainResponseCompound.to_json())

# convert the object into a dict
domain_response_compound_dict = domain_response_compound_instance.to_dict()
# create an instance of DomainResponseCompound from a dict
domain_response_compound_from_dict = DomainResponseCompound.from_dict(domain_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


