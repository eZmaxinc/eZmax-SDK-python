# CreditcardmerchantGetListV1Response

Response for GET /1/object/creditcardmerchant/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CreditcardmerchantGetListV1ResponseMPayload**](CreditcardmerchantGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardmerchant_get_list_v1_response import CreditcardmerchantGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardmerchantGetListV1Response from a JSON string
creditcardmerchant_get_list_v1_response_instance = CreditcardmerchantGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(CreditcardmerchantGetListV1Response.to_json())

# convert the object into a dict
creditcardmerchant_get_list_v1_response_dict = creditcardmerchant_get_list_v1_response_instance.to_dict()
# create an instance of CreditcardmerchantGetListV1Response from a dict
creditcardmerchant_get_list_v1_response_from_dict = CreditcardmerchantGetListV1Response.from_dict(creditcardmerchant_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


