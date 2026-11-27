# BrokerSyncDocumenttypechecklistV1Response

Response for POST /1/object/broker/{pkiBrokerID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BrokerSyncDocumenttypechecklistV1ResponseMPayload**](BrokerSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.broker_sync_documenttypechecklist_v1_response import BrokerSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerSyncDocumenttypechecklistV1Response from a JSON string
broker_sync_documenttypechecklist_v1_response_instance = BrokerSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(BrokerSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
broker_sync_documenttypechecklist_v1_response_dict = broker_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of BrokerSyncDocumenttypechecklistV1Response from a dict
broker_sync_documenttypechecklist_v1_response_from_dict = BrokerSyncDocumenttypechecklistV1Response.from_dict(broker_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


