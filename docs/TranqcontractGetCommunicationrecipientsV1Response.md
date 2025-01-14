# TranqcontractGetCommunicationrecipientsV1Response

Response for GET /1/object/tranqcontract/{pkiTranqcontractID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**TranqcontractGetCommunicationrecipientsV1ResponseMPayload**](TranqcontractGetCommunicationrecipientsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.tranqcontract_get_communicationrecipients_v1_response import TranqcontractGetCommunicationrecipientsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of TranqcontractGetCommunicationrecipientsV1Response from a JSON string
tranqcontract_get_communicationrecipients_v1_response_instance = TranqcontractGetCommunicationrecipientsV1Response.from_json(json)
# print the JSON string representation of the object
print(TranqcontractGetCommunicationrecipientsV1Response.to_json())

# convert the object into a dict
tranqcontract_get_communicationrecipients_v1_response_dict = tranqcontract_get_communicationrecipients_v1_response_instance.to_dict()
# create an instance of TranqcontractGetCommunicationrecipientsV1Response from a dict
tranqcontract_get_communicationrecipients_v1_response_from_dict = TranqcontractGetCommunicationrecipientsV1Response.from_dict(tranqcontract_get_communicationrecipients_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


