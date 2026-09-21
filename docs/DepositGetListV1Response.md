# DepositGetListV1Response

Response for GET /1/object/deposit/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DepositGetListV1ResponseMPayload**](DepositGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.deposit_get_list_v1_response import DepositGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DepositGetListV1Response from a JSON string
deposit_get_list_v1_response_instance = DepositGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(DepositGetListV1Response.to_json())

# convert the object into a dict
deposit_get_list_v1_response_dict = deposit_get_list_v1_response_instance.to_dict()
# create an instance of DepositGetListV1Response from a dict
deposit_get_list_v1_response_from_dict = DepositGetListV1Response.from_dict(deposit_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


