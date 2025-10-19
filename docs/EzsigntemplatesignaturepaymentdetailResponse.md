# EzsigntemplatesignaturepaymentdetailResponse

An Ezsigntemplatesignaturepaymentdetail Object

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
from eZmaxApi.models.ezsigntemplatesignaturepaymentdetail_response import EzsigntemplatesignaturepaymentdetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignaturepaymentdetailResponse from a JSON string
ezsigntemplatesignaturepaymentdetail_response_instance = EzsigntemplatesignaturepaymentdetailResponse.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignaturepaymentdetailResponse.to_json())

# convert the object into a dict
ezsigntemplatesignaturepaymentdetail_response_dict = ezsigntemplatesignaturepaymentdetail_response_instance.to_dict()
# create an instance of EzsigntemplatesignaturepaymentdetailResponse from a dict
ezsigntemplatesignaturepaymentdetail_response_from_dict = EzsigntemplatesignaturepaymentdetailResponse.from_dict(ezsigntemplatesignaturepaymentdetail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


