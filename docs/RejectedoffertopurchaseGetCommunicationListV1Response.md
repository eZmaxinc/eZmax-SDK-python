# RejectedoffertopurchaseGetCommunicationListV1Response

Response for GET /1/object/rejectedoffertopurchase/{pkiRejectedoffertopurchaseID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**RejectedoffertopurchaseGetCommunicationListV1ResponseMPayload**](RejectedoffertopurchaseGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.rejectedoffertopurchase_get_communication_list_v1_response import RejectedoffertopurchaseGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of RejectedoffertopurchaseGetCommunicationListV1Response from a JSON string
rejectedoffertopurchase_get_communication_list_v1_response_instance = RejectedoffertopurchaseGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print(RejectedoffertopurchaseGetCommunicationListV1Response.to_json())

# convert the object into a dict
rejectedoffertopurchase_get_communication_list_v1_response_dict = rejectedoffertopurchase_get_communication_list_v1_response_instance.to_dict()
# create an instance of RejectedoffertopurchaseGetCommunicationListV1Response from a dict
rejectedoffertopurchase_get_communication_list_v1_response_from_dict = RejectedoffertopurchaseGetCommunicationListV1Response.from_dict(rejectedoffertopurchase_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


