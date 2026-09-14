# BankaccountGetCommunicationListV1ResponseMPayload

Response for GET /1/object/bankaccount/{pkiBankaccountID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communication** | [**List[CustomCommunicationListElementResponse]**](CustomCommunicationListElementResponse.md) |  | 

## Example

```python
from eZmaxApi.models.bankaccount_get_communication_list_v1_response_m_payload import BankaccountGetCommunicationListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountGetCommunicationListV1ResponseMPayload from a JSON string
bankaccount_get_communication_list_v1_response_m_payload_instance = BankaccountGetCommunicationListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BankaccountGetCommunicationListV1ResponseMPayload.to_json())

# convert the object into a dict
bankaccount_get_communication_list_v1_response_m_payload_dict = bankaccount_get_communication_list_v1_response_m_payload_instance.to_dict()
# create an instance of BankaccountGetCommunicationListV1ResponseMPayload from a dict
bankaccount_get_communication_list_v1_response_m_payload_from_dict = BankaccountGetCommunicationListV1ResponseMPayload.from_dict(bankaccount_get_communication_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


