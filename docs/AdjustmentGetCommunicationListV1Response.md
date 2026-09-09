# AdjustmentGetCommunicationListV1Response

Response for GET /1/object/adjustment/{pkiAdjustmentID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AdjustmentGetCommunicationListV1ResponseMPayload**](AdjustmentGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.adjustment_get_communication_list_v1_response import AdjustmentGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentGetCommunicationListV1Response from a JSON string
adjustment_get_communication_list_v1_response_instance = AdjustmentGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print(AdjustmentGetCommunicationListV1Response.to_json())

# convert the object into a dict
adjustment_get_communication_list_v1_response_dict = adjustment_get_communication_list_v1_response_instance.to_dict()
# create an instance of AdjustmentGetCommunicationListV1Response from a dict
adjustment_get_communication_list_v1_response_from_dict = AdjustmentGetCommunicationListV1Response.from_dict(adjustment_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


