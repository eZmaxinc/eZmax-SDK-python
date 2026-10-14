# ReconciliationGetCommunicationrecipientsV1Response

Response for GET /1/object/reconciliation/{pkiReconciliationID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ReconciliationGetCommunicationrecipientsV1ResponseMPayload**](ReconciliationGetCommunicationrecipientsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.reconciliation_get_communicationrecipients_v1_response import ReconciliationGetCommunicationrecipientsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationGetCommunicationrecipientsV1Response from a JSON string
reconciliation_get_communicationrecipients_v1_response_instance = ReconciliationGetCommunicationrecipientsV1Response.from_json(json)
# print the JSON string representation of the object
print(ReconciliationGetCommunicationrecipientsV1Response.to_json())

# convert the object into a dict
reconciliation_get_communicationrecipients_v1_response_dict = reconciliation_get_communicationrecipients_v1_response_instance.to_dict()
# create an instance of ReconciliationGetCommunicationrecipientsV1Response from a dict
reconciliation_get_communicationrecipients_v1_response_from_dict = ReconciliationGetCommunicationrecipientsV1Response.from_dict(reconciliation_get_communicationrecipients_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


