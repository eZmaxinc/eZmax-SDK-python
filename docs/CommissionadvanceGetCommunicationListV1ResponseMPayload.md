# CommissionadvanceGetCommunicationListV1ResponseMPayload

Response for GET /1/object/commissionadvance/{pkiCommissionadvanceID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communication** | [**List[CustomCommunicationListElementResponse]**](CustomCommunicationListElementResponse.md) |  | 

## Example

```python
from eZmaxApi.models.commissionadvance_get_communication_list_v1_response_m_payload import CommissionadvanceGetCommunicationListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionadvanceGetCommunicationListV1ResponseMPayload from a JSON string
commissionadvance_get_communication_list_v1_response_m_payload_instance = CommissionadvanceGetCommunicationListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CommissionadvanceGetCommunicationListV1ResponseMPayload.to_json())

# convert the object into a dict
commissionadvance_get_communication_list_v1_response_m_payload_dict = commissionadvance_get_communication_list_v1_response_m_payload_instance.to_dict()
# create an instance of CommissionadvanceGetCommunicationListV1ResponseMPayload from a dict
commissionadvance_get_communication_list_v1_response_m_payload_from_dict = CommissionadvanceGetCommunicationListV1ResponseMPayload.from_dict(commissionadvance_get_communication_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


