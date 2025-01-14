# CustomDnsrecordResponse

A Custom Dnsrecord Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_dnsrecord_type** | **str** | The type of the Dnsrecord | 
**e_dnsrecord_validation** | **str** | The validation of the Dnsrecord | 
**s_dnsrecord_name** | **str** | The name of the Dnsrecord | 
**s_dnsrecord_value** | **str** | The value of the Dnsrecord | [optional] 
**s_dnsrecord_expectedvalue** | **str** | The expected value of the Dnsrecord | [optional] 
**b_dnsrecord_must_match** | **bool** | Whether the Dnsrecord must match or not | 

## Example

```python
from eZmaxApi.models.custom_dnsrecord_response import CustomDnsrecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDnsrecordResponse from a JSON string
custom_dnsrecord_response_instance = CustomDnsrecordResponse.from_json(json)
# print the JSON string representation of the object
print(CustomDnsrecordResponse.to_json())

# convert the object into a dict
custom_dnsrecord_response_dict = custom_dnsrecord_response_instance.to_dict()
# create an instance of CustomDnsrecordResponse from a dict
custom_dnsrecord_response_from_dict = CustomDnsrecordResponse.from_dict(custom_dnsrecord_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


