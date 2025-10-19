# EzsigntemplatesignaturepaymentdetailResponseCompound

An Ezsigntemplatesignaturepaymentdetail Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatesignaturepaymentdetail_id** | **int** | The unique ID of the Ezsignsignaturepaymentdetail | 
**fki_glaccountcontainer_id** | **int** | The unique ID of the Glaccountcontainer | [optional] 
**t_ezsigntemplatesignaturepaymentdetail_description** | **str** | A description for the Ezsignsignaturepaymentdetail. | 
**d_ezsigntemplatesignaturepaymentdetail_amount** | **str** | The amount of the for the Ezsignsignaturepaymentdetail | 
**e_ezsigntemplatesignaturepaymentdetail_taxable** | [**FieldEEzsigntemplatesignaturepaymentdetailTaxable**](FieldEEzsigntemplatesignaturepaymentdetailTaxable.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignaturepaymentdetail_response_compound import EzsigntemplatesignaturepaymentdetailResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignaturepaymentdetailResponseCompound from a JSON string
ezsigntemplatesignaturepaymentdetail_response_compound_instance = EzsigntemplatesignaturepaymentdetailResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignaturepaymentdetailResponseCompound.to_json())

# convert the object into a dict
ezsigntemplatesignaturepaymentdetail_response_compound_dict = ezsigntemplatesignaturepaymentdetail_response_compound_instance.to_dict()
# create an instance of EzsigntemplatesignaturepaymentdetailResponseCompound from a dict
ezsigntemplatesignaturepaymentdetail_response_compound_from_dict = EzsigntemplatesignaturepaymentdetailResponseCompound.from_dict(ezsigntemplatesignaturepaymentdetail_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


