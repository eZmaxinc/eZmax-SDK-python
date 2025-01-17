# PaymenttermGetListV1Response

Response for GET /1/object/paymentterm/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PaymenttermGetListV1ResponseMPayload**](PaymenttermGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.paymentterm_get_list_v1_response import PaymenttermGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymenttermGetListV1Response from a JSON string
paymentterm_get_list_v1_response_instance = PaymenttermGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(PaymenttermGetListV1Response.to_json())

# convert the object into a dict
paymentterm_get_list_v1_response_dict = paymentterm_get_list_v1_response_instance.to_dict()
# create an instance of PaymenttermGetListV1Response from a dict
paymentterm_get_list_v1_response_from_dict = PaymenttermGetListV1Response.from_dict(paymentterm_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


