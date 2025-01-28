# CreditcardmerchantDeleteObjectV1Response

Response for DELETE /1/object/creditcardmerchant/{pkiCreditcardmerchantID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.creditcardmerchant_delete_object_v1_response import CreditcardmerchantDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardmerchantDeleteObjectV1Response from a JSON string
creditcardmerchant_delete_object_v1_response_instance = CreditcardmerchantDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(CreditcardmerchantDeleteObjectV1Response.to_json())

# convert the object into a dict
creditcardmerchant_delete_object_v1_response_dict = creditcardmerchant_delete_object_v1_response_instance.to_dict()
# create an instance of CreditcardmerchantDeleteObjectV1Response from a dict
creditcardmerchant_delete_object_v1_response_from_dict = CreditcardmerchantDeleteObjectV1Response.from_dict(creditcardmerchant_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


