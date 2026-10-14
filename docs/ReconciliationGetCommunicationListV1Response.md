# ReconciliationGetCommunicationListV1Response

Response for GET /1/object/reconciliation/{pkiReconciliationID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ReconciliationGetCommunicationListV1ResponseMPayload**](ReconciliationGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.reconciliation_get_communication_list_v1_response import ReconciliationGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationGetCommunicationListV1Response from a JSON string
reconciliation_get_communication_list_v1_response_instance = ReconciliationGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print(ReconciliationGetCommunicationListV1Response.to_json())

# convert the object into a dict
reconciliation_get_communication_list_v1_response_dict = reconciliation_get_communication_list_v1_response_instance.to_dict()
# create an instance of ReconciliationGetCommunicationListV1Response from a dict
reconciliation_get_communication_list_v1_response_from_dict = ReconciliationGetCommunicationListV1Response.from_dict(reconciliation_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


