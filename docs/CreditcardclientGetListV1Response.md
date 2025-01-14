# CreditcardclientGetListV1Response

Response for GET /1/object/creditcardclient/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CreditcardclientGetListV1ResponseMPayload**](CreditcardclientGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardclient_get_list_v1_response import CreditcardclientGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardclientGetListV1Response from a JSON string
creditcardclient_get_list_v1_response_instance = CreditcardclientGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(CreditcardclientGetListV1Response.to_json())

# convert the object into a dict
creditcardclient_get_list_v1_response_dict = creditcardclient_get_list_v1_response_instance.to_dict()
# create an instance of CreditcardclientGetListV1Response from a dict
creditcardclient_get_list_v1_response_from_dict = CreditcardclientGetListV1Response.from_dict(creditcardclient_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


