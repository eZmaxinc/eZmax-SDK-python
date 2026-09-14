# CommissionadvanceGetCommunicationsendersV1ResponseMPayload

Response for GET /1/object/commissionadvance/{pkiCommissionadvanceID}/getCommunicationsenders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationsenders** | [**List[CustomCommunicationsenderResponse]**](CustomCommunicationsenderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.commissionadvance_get_communicationsenders_v1_response_m_payload import CommissionadvanceGetCommunicationsendersV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionadvanceGetCommunicationsendersV1ResponseMPayload from a JSON string
commissionadvance_get_communicationsenders_v1_response_m_payload_instance = CommissionadvanceGetCommunicationsendersV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CommissionadvanceGetCommunicationsendersV1ResponseMPayload.to_json())

# convert the object into a dict
commissionadvance_get_communicationsenders_v1_response_m_payload_dict = commissionadvance_get_communicationsenders_v1_response_m_payload_instance.to_dict()
# create an instance of CommissionadvanceGetCommunicationsendersV1ResponseMPayload from a dict
commissionadvance_get_communicationsenders_v1_response_m_payload_from_dict = CommissionadvanceGetCommunicationsendersV1ResponseMPayload.from_dict(commissionadvance_get_communicationsenders_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


