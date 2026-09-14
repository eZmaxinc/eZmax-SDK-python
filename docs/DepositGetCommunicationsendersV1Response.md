# DepositGetCommunicationsendersV1Response

Response for GET /1/object/deposit/{pkiDepositID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DepositGetCommunicationsendersV1ResponseMPayload**](DepositGetCommunicationsendersV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.deposit_get_communicationsenders_v1_response import DepositGetCommunicationsendersV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DepositGetCommunicationsendersV1Response from a JSON string
deposit_get_communicationsenders_v1_response_instance = DepositGetCommunicationsendersV1Response.from_json(json)
# print the JSON string representation of the object
print(DepositGetCommunicationsendersV1Response.to_json())

# convert the object into a dict
deposit_get_communicationsenders_v1_response_dict = deposit_get_communicationsenders_v1_response_instance.to_dict()
# create an instance of DepositGetCommunicationsendersV1Response from a dict
deposit_get_communicationsenders_v1_response_from_dict = DepositGetCommunicationsendersV1Response.from_dict(deposit_get_communicationsenders_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


