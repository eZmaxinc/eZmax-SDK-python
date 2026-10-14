# ReconciliationGetCommunicationCountV1Response

Response for GET /1/object/reconciliation/{pkiReconciliationID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ReconciliationGetCommunicationCountV1ResponseMPayload**](ReconciliationGetCommunicationCountV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.reconciliation_get_communication_count_v1_response import ReconciliationGetCommunicationCountV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationGetCommunicationCountV1Response from a JSON string
reconciliation_get_communication_count_v1_response_instance = ReconciliationGetCommunicationCountV1Response.from_json(json)
# print the JSON string representation of the object
print(ReconciliationGetCommunicationCountV1Response.to_json())

# convert the object into a dict
reconciliation_get_communication_count_v1_response_dict = reconciliation_get_communication_count_v1_response_instance.to_dict()
# create an instance of ReconciliationGetCommunicationCountV1Response from a dict
reconciliation_get_communication_count_v1_response_from_dict = ReconciliationGetCommunicationCountV1Response.from_dict(reconciliation_get_communication_count_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


