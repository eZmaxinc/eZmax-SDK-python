# CreditcardclientCreateObjectV1Response

Response for POST /1/object/creditcardclient

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CreditcardclientCreateObjectV1ResponseMPayload**](CreditcardclientCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardclient_create_object_v1_response import CreditcardclientCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardclientCreateObjectV1Response from a JSON string
creditcardclient_create_object_v1_response_instance = CreditcardclientCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(CreditcardclientCreateObjectV1Response.to_json())

# convert the object into a dict
creditcardclient_create_object_v1_response_dict = creditcardclient_create_object_v1_response_instance.to_dict()
# create an instance of CreditcardclientCreateObjectV1Response from a dict
creditcardclient_create_object_v1_response_form_dict = creditcardclient_create_object_v1_response.from_dict(creditcardclient_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


