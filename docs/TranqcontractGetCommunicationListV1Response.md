# TranqcontractGetCommunicationListV1Response

Response for GET /1/object/tranqcontract/{pkiTranqcontractID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**TranqcontractGetCommunicationListV1ResponseMPayload**](TranqcontractGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.tranqcontract_get_communication_list_v1_response import TranqcontractGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of TranqcontractGetCommunicationListV1Response from a JSON string
tranqcontract_get_communication_list_v1_response_instance = TranqcontractGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print(TranqcontractGetCommunicationListV1Response.to_json())

# convert the object into a dict
tranqcontract_get_communication_list_v1_response_dict = tranqcontract_get_communication_list_v1_response_instance.to_dict()
# create an instance of TranqcontractGetCommunicationListV1Response from a dict
tranqcontract_get_communication_list_v1_response_from_dict = TranqcontractGetCommunicationListV1Response.from_dict(tranqcontract_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


