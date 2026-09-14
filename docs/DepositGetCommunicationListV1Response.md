# DepositGetCommunicationListV1Response

Response for GET /1/object/deposit/{pkiDepositID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DepositGetCommunicationListV1ResponseMPayload**](DepositGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.deposit_get_communication_list_v1_response import DepositGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DepositGetCommunicationListV1Response from a JSON string
deposit_get_communication_list_v1_response_instance = DepositGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print(DepositGetCommunicationListV1Response.to_json())

# convert the object into a dict
deposit_get_communication_list_v1_response_dict = deposit_get_communication_list_v1_response_instance.to_dict()
# create an instance of DepositGetCommunicationListV1Response from a dict
deposit_get_communication_list_v1_response_from_dict = DepositGetCommunicationListV1Response.from_dict(deposit_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


