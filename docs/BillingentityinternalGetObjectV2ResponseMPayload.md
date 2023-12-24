# BillingentityinternalGetObjectV2ResponseMPayload

Payload for GET /2/object/billingentityinternal/{pkiBillingentityinternalID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_billingentityinternal** | [**BillingentityinternalResponseCompound**](BillingentityinternalResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.billingentityinternal_get_object_v2_response_m_payload import BillingentityinternalGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalGetObjectV2ResponseMPayload from a JSON string
billingentityinternal_get_object_v2_response_m_payload_instance = BillingentityinternalGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print BillingentityinternalGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
billingentityinternal_get_object_v2_response_m_payload_dict = billingentityinternal_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of BillingentityinternalGetObjectV2ResponseMPayload from a dict
billingentityinternal_get_object_v2_response_m_payload_form_dict = billingentityinternal_get_object_v2_response_m_payload.from_dict(billingentityinternal_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


