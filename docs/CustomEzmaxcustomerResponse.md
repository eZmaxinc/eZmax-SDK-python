# CustomEzmaxcustomerResponse

A Ezmaxcustomer Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fks_ezmaxcustomer_code** | **str** | The Ezmaxcustomer code | 
**fki_systemconfigurationtype_id** | **int** | The unique ID of the Systemconfigurationtype | 
**obj_ezmaxcustomer_company** | [**MultilingualEzmaxcustomerCompany**](MultilingualEzmaxcustomerCompany.md) |  | 

## Example

```python
from eZmaxApi.models.custom_ezmaxcustomer_response import CustomEzmaxcustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzmaxcustomerResponse from a JSON string
custom_ezmaxcustomer_response_instance = CustomEzmaxcustomerResponse.from_json(json)
# print the JSON string representation of the object
print(CustomEzmaxcustomerResponse.to_json())

# convert the object into a dict
custom_ezmaxcustomer_response_dict = custom_ezmaxcustomer_response_instance.to_dict()
# create an instance of CustomEzmaxcustomerResponse from a dict
custom_ezmaxcustomer_response_from_dict = CustomEzmaxcustomerResponse.from_dict(custom_ezmaxcustomer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


