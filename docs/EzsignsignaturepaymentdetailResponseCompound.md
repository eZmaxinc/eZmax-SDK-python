# EzsignsignaturepaymentdetailResponseCompound

An Ezsignsignaturepaymentdetail Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignsignaturepaymentdetail_id** | **int** | The unique ID of the Ezsignsignaturepaymentdetail | 
**fki_glaccountcontainer_id** | **int** | The unique ID of the Glaccountcontainer | [optional] 
**t_ezsignsignaturepaymentdetail_description** | **str** | A description for the Ezsignsignaturepaymentdetail. | 
**d_ezsignsignaturepaymentdetail_amount** | **str** | The amount of the for the Ezsignsignaturepaymentdetail | 
**e_ezsignsignaturepaymentdetail_taxable** | [**FieldEEzsignsignaturepaymentdetailTaxable**](FieldEEzsignsignaturepaymentdetailTaxable.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignaturepaymentdetail_response_compound import EzsignsignaturepaymentdetailResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignaturepaymentdetailResponseCompound from a JSON string
ezsignsignaturepaymentdetail_response_compound_instance = EzsignsignaturepaymentdetailResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignsignaturepaymentdetailResponseCompound.to_json())

# convert the object into a dict
ezsignsignaturepaymentdetail_response_compound_dict = ezsignsignaturepaymentdetail_response_compound_instance.to_dict()
# create an instance of EzsignsignaturepaymentdetailResponseCompound from a dict
ezsignsignaturepaymentdetail_response_compound_from_dict = EzsignsignaturepaymentdetailResponseCompound.from_dict(ezsignsignaturepaymentdetail_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


