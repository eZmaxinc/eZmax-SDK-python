# EzsigntemplatesignaturepaymentdetailRequestCompound

An Ezsigntemplatesignaturepaymentdetail Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatesignaturepaymentdetail_id** | **int** | The unique ID of the Ezsignsignaturepaymentdetail | [optional] 
**fki_glaccountcontainer_id** | **int** | The unique ID of the Glaccountcontainer | 
**t_ezsigntemplatesignaturepaymentdetail_description** | **str** | A description for the Ezsignsignaturepaymentdetail. | 
**d_ezsigntemplatesignaturepaymentdetail_amount** | **str** | The amount of the for the Ezsignsignaturepaymentdetail | 
**e_ezsigntemplatesignaturepaymentdetail_taxable** | [**FieldEEzsigntemplatesignaturepaymentdetailTaxable**](FieldEEzsigntemplatesignaturepaymentdetailTaxable.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignaturepaymentdetail_request_compound import EzsigntemplatesignaturepaymentdetailRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignaturepaymentdetailRequestCompound from a JSON string
ezsigntemplatesignaturepaymentdetail_request_compound_instance = EzsigntemplatesignaturepaymentdetailRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignaturepaymentdetailRequestCompound.to_json())

# convert the object into a dict
ezsigntemplatesignaturepaymentdetail_request_compound_dict = ezsigntemplatesignaturepaymentdetail_request_compound_instance.to_dict()
# create an instance of EzsigntemplatesignaturepaymentdetailRequestCompound from a dict
ezsigntemplatesignaturepaymentdetail_request_compound_from_dict = EzsigntemplatesignaturepaymentdetailRequestCompound.from_dict(ezsigntemplatesignaturepaymentdetail_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


