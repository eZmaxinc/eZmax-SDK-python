# EzsignsignaturepaymentdetailResponse

An Ezsignsignaturepaymentdetail Object

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
from eZmaxApi.models.ezsignsignaturepaymentdetail_response import EzsignsignaturepaymentdetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignaturepaymentdetailResponse from a JSON string
ezsignsignaturepaymentdetail_response_instance = EzsignsignaturepaymentdetailResponse.from_json(json)
# print the JSON string representation of the object
print(EzsignsignaturepaymentdetailResponse.to_json())

# convert the object into a dict
ezsignsignaturepaymentdetail_response_dict = ezsignsignaturepaymentdetail_response_instance.to_dict()
# create an instance of EzsignsignaturepaymentdetailResponse from a dict
ezsignsignaturepaymentdetail_response_from_dict = EzsignsignaturepaymentdetailResponse.from_dict(ezsignsignaturepaymentdetail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


