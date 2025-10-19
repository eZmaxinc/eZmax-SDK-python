# BrokerImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/broker/{pkiBrokerID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.broker_import_into_edmv1_response_m_payload import BrokerImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerImportIntoEDMV1ResponseMPayload from a JSON string
broker_import_into_edmv1_response_m_payload_instance = BrokerImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BrokerImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
broker_import_into_edmv1_response_m_payload_dict = broker_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of BrokerImportIntoEDMV1ResponseMPayload from a dict
broker_import_into_edmv1_response_m_payload_from_dict = BrokerImportIntoEDMV1ResponseMPayload.from_dict(broker_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


