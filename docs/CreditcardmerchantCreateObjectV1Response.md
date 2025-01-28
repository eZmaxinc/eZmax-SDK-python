# CreditcardmerchantCreateObjectV1Response

Response for POST /1/object/creditcardmerchant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CreditcardmerchantCreateObjectV1ResponseMPayload**](CreditcardmerchantCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardmerchant_create_object_v1_response import CreditcardmerchantCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardmerchantCreateObjectV1Response from a JSON string
creditcardmerchant_create_object_v1_response_instance = CreditcardmerchantCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(CreditcardmerchantCreateObjectV1Response.to_json())

# convert the object into a dict
creditcardmerchant_create_object_v1_response_dict = creditcardmerchant_create_object_v1_response_instance.to_dict()
# create an instance of CreditcardmerchantCreateObjectV1Response from a dict
creditcardmerchant_create_object_v1_response_from_dict = CreditcardmerchantCreateObjectV1Response.from_dict(creditcardmerchant_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


