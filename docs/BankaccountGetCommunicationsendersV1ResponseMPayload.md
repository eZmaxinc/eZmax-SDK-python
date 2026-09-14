# BankaccountGetCommunicationsendersV1ResponseMPayload

Response for GET /1/object/bankaccount/{pkiBankaccountID}/getCommunicationsenders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationsenders** | [**List[CustomCommunicationsenderResponse]**](CustomCommunicationsenderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.bankaccount_get_communicationsenders_v1_response_m_payload import BankaccountGetCommunicationsendersV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountGetCommunicationsendersV1ResponseMPayload from a JSON string
bankaccount_get_communicationsenders_v1_response_m_payload_instance = BankaccountGetCommunicationsendersV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BankaccountGetCommunicationsendersV1ResponseMPayload.to_json())

# convert the object into a dict
bankaccount_get_communicationsenders_v1_response_m_payload_dict = bankaccount_get_communicationsenders_v1_response_m_payload_instance.to_dict()
# create an instance of BankaccountGetCommunicationsendersV1ResponseMPayload from a dict
bankaccount_get_communicationsenders_v1_response_m_payload_from_dict = BankaccountGetCommunicationsendersV1ResponseMPayload.from_dict(bankaccount_get_communicationsenders_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


