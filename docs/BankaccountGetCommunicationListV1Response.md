# BankaccountGetCommunicationListV1Response

Response for GET /1/object/bankaccount/{pkiBankaccountID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BankaccountGetCommunicationListV1ResponseMPayload**](BankaccountGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.bankaccount_get_communication_list_v1_response import BankaccountGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountGetCommunicationListV1Response from a JSON string
bankaccount_get_communication_list_v1_response_instance = BankaccountGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print(BankaccountGetCommunicationListV1Response.to_json())

# convert the object into a dict
bankaccount_get_communication_list_v1_response_dict = bankaccount_get_communication_list_v1_response_instance.to_dict()
# create an instance of BankaccountGetCommunicationListV1Response from a dict
bankaccount_get_communication_list_v1_response_from_dict = BankaccountGetCommunicationListV1Response.from_dict(bankaccount_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


