# BillingentityinternalEditObjectV1Request

Request for PUT /1/object/billingentityinternal/{pkiBillingentityinternalID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_billingentityinternal** | [**BillingentityinternalRequestCompound**](BillingentityinternalRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.billingentityinternal_edit_object_v1_request import BillingentityinternalEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalEditObjectV1Request from a JSON string
billingentityinternal_edit_object_v1_request_instance = BillingentityinternalEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(BillingentityinternalEditObjectV1Request.to_json())

# convert the object into a dict
billingentityinternal_edit_object_v1_request_dict = billingentityinternal_edit_object_v1_request_instance.to_dict()
# create an instance of BillingentityinternalEditObjectV1Request from a dict
billingentityinternal_edit_object_v1_request_from_dict = BillingentityinternalEditObjectV1Request.from_dict(billingentityinternal_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


