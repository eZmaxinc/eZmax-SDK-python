# RejectedoffertopurchaseGetListV1Response

Response for GET /1/object/rejectedoffertopurchase/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**RejectedoffertopurchaseGetListV1ResponseMPayload**](RejectedoffertopurchaseGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.rejectedoffertopurchase_get_list_v1_response import RejectedoffertopurchaseGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of RejectedoffertopurchaseGetListV1Response from a JSON string
rejectedoffertopurchase_get_list_v1_response_instance = RejectedoffertopurchaseGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(RejectedoffertopurchaseGetListV1Response.to_json())

# convert the object into a dict
rejectedoffertopurchase_get_list_v1_response_dict = rejectedoffertopurchase_get_list_v1_response_instance.to_dict()
# create an instance of RejectedoffertopurchaseGetListV1Response from a dict
rejectedoffertopurchase_get_list_v1_response_from_dict = RejectedoffertopurchaseGetListV1Response.from_dict(rejectedoffertopurchase_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


