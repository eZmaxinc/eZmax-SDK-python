# DeposittransitchequeGetCommunicationListV1Response

Response for GET /1/object/deposittransitcheque/{pkiDeposittransitchequeID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DeposittransitchequeGetCommunicationListV1ResponseMPayload**](DeposittransitchequeGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.deposittransitcheque_get_communication_list_v1_response import DeposittransitchequeGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeposittransitchequeGetCommunicationListV1Response from a JSON string
deposittransitcheque_get_communication_list_v1_response_instance = DeposittransitchequeGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print(DeposittransitchequeGetCommunicationListV1Response.to_json())

# convert the object into a dict
deposittransitcheque_get_communication_list_v1_response_dict = deposittransitcheque_get_communication_list_v1_response_instance.to_dict()
# create an instance of DeposittransitchequeGetCommunicationListV1Response from a dict
deposittransitcheque_get_communication_list_v1_response_from_dict = DeposittransitchequeGetCommunicationListV1Response.from_dict(deposittransitcheque_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


