# BillingentityinternalResponse

A Billingentityinternal Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_billingentityinternal_id** | **int** | The unique ID of the Billingentityinternal. | 
**obj_billingentityinternal_description** | [**MultilingualBillingentityinternalDescription**](MultilingualBillingentityinternalDescription.md) |  | 

## Example

```python
from eZmaxApi.models.billingentityinternal_response import BillingentityinternalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalResponse from a JSON string
billingentityinternal_response_instance = BillingentityinternalResponse.from_json(json)
# print the JSON string representation of the object
print(BillingentityinternalResponse.to_json())

# convert the object into a dict
billingentityinternal_response_dict = billingentityinternal_response_instance.to_dict()
# create an instance of BillingentityinternalResponse from a dict
billingentityinternal_response_from_dict = BillingentityinternalResponse.from_dict(billingentityinternal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


