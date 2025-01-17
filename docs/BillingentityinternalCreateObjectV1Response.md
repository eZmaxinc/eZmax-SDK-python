# BillingentityinternalCreateObjectV1Response

Response for POST /1/object/billingentityinternal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**BillingentityinternalCreateObjectV1ResponseMPayload**](BillingentityinternalCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.billingentityinternal_create_object_v1_response import BillingentityinternalCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalCreateObjectV1Response from a JSON string
billingentityinternal_create_object_v1_response_instance = BillingentityinternalCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(BillingentityinternalCreateObjectV1Response.to_json())

# convert the object into a dict
billingentityinternal_create_object_v1_response_dict = billingentityinternal_create_object_v1_response_instance.to_dict()
# create an instance of BillingentityinternalCreateObjectV1Response from a dict
billingentityinternal_create_object_v1_response_from_dict = BillingentityinternalCreateObjectV1Response.from_dict(billingentityinternal_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


