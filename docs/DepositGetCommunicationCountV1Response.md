# DepositGetCommunicationCountV1Response

Response for GET /1/object/deposit/{pkiDepositID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DepositGetCommunicationCountV1ResponseMPayload**](DepositGetCommunicationCountV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.deposit_get_communication_count_v1_response import DepositGetCommunicationCountV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DepositGetCommunicationCountV1Response from a JSON string
deposit_get_communication_count_v1_response_instance = DepositGetCommunicationCountV1Response.from_json(json)
# print the JSON string representation of the object
print(DepositGetCommunicationCountV1Response.to_json())

# convert the object into a dict
deposit_get_communication_count_v1_response_dict = deposit_get_communication_count_v1_response_instance.to_dict()
# create an instance of DepositGetCommunicationCountV1Response from a dict
deposit_get_communication_count_v1_response_from_dict = DepositGetCommunicationCountV1Response.from_dict(deposit_get_communication_count_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


