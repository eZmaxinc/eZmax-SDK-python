# BillingentityinternalGetListV1Response

Response for GET /1/object/billingentityinternal/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**BillingentityinternalGetListV1ResponseMPayload**](BillingentityinternalGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.billingentityinternal_get_list_v1_response import BillingentityinternalGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalGetListV1Response from a JSON string
billingentityinternal_get_list_v1_response_instance = BillingentityinternalGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(BillingentityinternalGetListV1Response.to_json())

# convert the object into a dict
billingentityinternal_get_list_v1_response_dict = billingentityinternal_get_list_v1_response_instance.to_dict()
# create an instance of BillingentityinternalGetListV1Response from a dict
billingentityinternal_get_list_v1_response_from_dict = BillingentityinternalGetListV1Response.from_dict(billingentityinternal_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


