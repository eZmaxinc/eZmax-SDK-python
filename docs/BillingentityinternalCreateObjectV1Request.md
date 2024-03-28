# BillingentityinternalCreateObjectV1Request

Request for POST /1/object/billingentityinternal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_billingentityinternal** | [**List[BillingentityinternalRequestCompound]**](BillingentityinternalRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.billingentityinternal_create_object_v1_request import BillingentityinternalCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalCreateObjectV1Request from a JSON string
billingentityinternal_create_object_v1_request_instance = BillingentityinternalCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(BillingentityinternalCreateObjectV1Request.to_json())

# convert the object into a dict
billingentityinternal_create_object_v1_request_dict = billingentityinternal_create_object_v1_request_instance.to_dict()
# create an instance of BillingentityinternalCreateObjectV1Request from a dict
billingentityinternal_create_object_v1_request_form_dict = billingentityinternal_create_object_v1_request.from_dict(billingentityinternal_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


