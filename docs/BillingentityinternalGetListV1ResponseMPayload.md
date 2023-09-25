# BillingentityinternalGetListV1ResponseMPayload

Payload for GET /1/object/billingentityinternal/getList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_row_returned** | **int** | The number of rows returned | 
**i_row_filtered** | **int** | The number of rows matching your filters (if any) or the total number of rows | 
**a_obj_billingentityinternal** | [**List[BillingentityinternalListElement]**](BillingentityinternalListElement.md) |  | 

## Example

```python
from eZmaxApi.models.billingentityinternal_get_list_v1_response_m_payload import BillingentityinternalGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalGetListV1ResponseMPayload from a JSON string
billingentityinternal_get_list_v1_response_m_payload_instance = BillingentityinternalGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print BillingentityinternalGetListV1ResponseMPayload.to_json()

# convert the object into a dict
billingentityinternal_get_list_v1_response_m_payload_dict = billingentityinternal_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of BillingentityinternalGetListV1ResponseMPayload from a dict
billingentityinternal_get_list_v1_response_m_payload_form_dict = billingentityinternal_get_list_v1_response_m_payload.from_dict(billingentityinternal_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


