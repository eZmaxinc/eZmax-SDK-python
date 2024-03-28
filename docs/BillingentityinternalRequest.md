# BillingentityinternalRequest

A Billingentityinternal Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_billingentityinternal_id** | **int** | The unique ID of the Billingentityinternal. | [optional] 
**obj_billingentityinternal_description** | [**MultilingualBillingentityinternalDescription**](MultilingualBillingentityinternalDescription.md) |  | 

## Example

```python
from eZmaxApi.models.billingentityinternal_request import BillingentityinternalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalRequest from a JSON string
billingentityinternal_request_instance = BillingentityinternalRequest.from_json(json)
# print the JSON string representation of the object
print(BillingentityinternalRequest.to_json())

# convert the object into a dict
billingentityinternal_request_dict = billingentityinternal_request_instance.to_dict()
# create an instance of BillingentityinternalRequest from a dict
billingentityinternal_request_form_dict = billingentityinternal_request.from_dict(billingentityinternal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


