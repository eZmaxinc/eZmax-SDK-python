# DomainResponseCompound

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
**a_obj_dnsrecord** | [**List[CustomDnsrecordResponse]**](CustomDnsrecordResponse.md) |  | 

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


