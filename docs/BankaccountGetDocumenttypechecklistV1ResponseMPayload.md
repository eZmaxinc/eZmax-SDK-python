# BankaccountGetDocumenttypechecklistV1ResponseMPayload

Response for GET /1/object/bankaccount/{pkiBankaccountID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.bankaccount_get_documenttypechecklist_v1_response_m_payload import BankaccountGetDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountGetDocumenttypechecklistV1ResponseMPayload from a JSON string
bankaccount_get_documenttypechecklist_v1_response_m_payload_instance = BankaccountGetDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BankaccountGetDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
bankaccount_get_documenttypechecklist_v1_response_m_payload_dict = bankaccount_get_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of BankaccountGetDocumenttypechecklistV1ResponseMPayload from a dict
bankaccount_get_documenttypechecklist_v1_response_m_payload_from_dict = BankaccountGetDocumenttypechecklistV1ResponseMPayload.from_dict(bankaccount_get_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


