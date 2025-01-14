# DomainListElement

A Domain List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_domain_id** | **int** | The unique ID of the Domain | 
**s_domain_name** | **str** | The name of the Domain | 

## Example

```python
from eZmaxApi.models.domain_list_element import DomainListElement

# TODO update the JSON string below
json = "{}"
# create an instance of DomainListElement from a JSON string
domain_list_element_instance = DomainListElement.from_json(json)
# print the JSON string representation of the object
print(DomainListElement.to_json())

# convert the object into a dict
domain_list_element_dict = domain_list_element_instance.to_dict()
# create an instance of DomainListElement from a dict
domain_list_element_from_dict = DomainListElement.from_dict(domain_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


