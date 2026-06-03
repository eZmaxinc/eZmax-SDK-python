# MultilingualEzmaxcustomerCompany

Company of the Ezmaxcustomer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_ezmaxcustomer_company1** | **str** | The company of the Ezmaxcustomer in French | [optional] 
**s_ezmaxcustomer_company2** | **str** | The company of the Ezmaxcustomer in English | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_ezmaxcustomer_company import MultilingualEzmaxcustomerCompany

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualEzmaxcustomerCompany from a JSON string
multilingual_ezmaxcustomer_company_instance = MultilingualEzmaxcustomerCompany.from_json(json)
# print the JSON string representation of the object
print(MultilingualEzmaxcustomerCompany.to_json())

# convert the object into a dict
multilingual_ezmaxcustomer_company_dict = multilingual_ezmaxcustomer_company_instance.to_dict()
# create an instance of MultilingualEzmaxcustomerCompany from a dict
multilingual_ezmaxcustomer_company_from_dict = MultilingualEzmaxcustomerCompany.from_dict(multilingual_ezmaxcustomer_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


