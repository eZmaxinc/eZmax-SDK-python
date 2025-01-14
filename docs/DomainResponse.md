# DomainResponse

A Domain Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_domain_id** | **int** | The unique ID of the Domain | 
**s_domain_name** | **str** | The name of the Domain | 
**b_domain_validdkim** | **bool** | Whether the DKIM is valid or not | 
**b_domain_validmailfrom** | **bool** | Whether the mail from is valid or not | 
**b_domain_validcustomer** | **bool** | Whether the customer has access to it or not | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 

## Example

```python
from eZmaxApi.models.domain_response import DomainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainResponse from a JSON string
domain_response_instance = DomainResponse.from_json(json)
# print the JSON string representation of the object
print(DomainResponse.to_json())

# convert the object into a dict
domain_response_dict = domain_response_instance.to_dict()
# create an instance of DomainResponse from a dict
domain_response_from_dict = DomainResponse.from_dict(domain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


