# BrokerSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/broker/{pkiBrokerID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.broker_sync_documenttypechecklist_v1_response_m_payload import BrokerSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
broker_sync_documenttypechecklist_v1_response_m_payload_instance = BrokerSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BrokerSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
broker_sync_documenttypechecklist_v1_response_m_payload_dict = broker_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of BrokerSyncDocumenttypechecklistV1ResponseMPayload from a dict
broker_sync_documenttypechecklist_v1_response_m_payload_from_dict = BrokerSyncDocumenttypechecklistV1ResponseMPayload.from_dict(broker_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


