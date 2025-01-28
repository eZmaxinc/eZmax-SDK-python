# CreditcardmerchantGetObjectV2ResponseMPayload

Payload for GET /2/object/creditcardmerchant/{pkiCreditcardmerchantID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_creditcardmerchant** | [**CreditcardmerchantResponseCompound**](CreditcardmerchantResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardmerchant_get_object_v2_response_m_payload import CreditcardmerchantGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardmerchantGetObjectV2ResponseMPayload from a JSON string
creditcardmerchant_get_object_v2_response_m_payload_instance = CreditcardmerchantGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CreditcardmerchantGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
creditcardmerchant_get_object_v2_response_m_payload_dict = creditcardmerchant_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of CreditcardmerchantGetObjectV2ResponseMPayload from a dict
creditcardmerchant_get_object_v2_response_m_payload_from_dict = CreditcardmerchantGetObjectV2ResponseMPayload.from_dict(creditcardmerchant_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


