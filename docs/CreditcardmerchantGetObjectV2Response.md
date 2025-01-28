# CreditcardmerchantGetObjectV2Response

Response for GET /2/object/creditcardmerchant/{pkiCreditcardmerchantID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CreditcardmerchantGetObjectV2ResponseMPayload**](CreditcardmerchantGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardmerchant_get_object_v2_response import CreditcardmerchantGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardmerchantGetObjectV2Response from a JSON string
creditcardmerchant_get_object_v2_response_instance = CreditcardmerchantGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(CreditcardmerchantGetObjectV2Response.to_json())

# convert the object into a dict
creditcardmerchant_get_object_v2_response_dict = creditcardmerchant_get_object_v2_response_instance.to_dict()
# create an instance of CreditcardmerchantGetObjectV2Response from a dict
creditcardmerchant_get_object_v2_response_from_dict = CreditcardmerchantGetObjectV2Response.from_dict(creditcardmerchant_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


