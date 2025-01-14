# RejectedoffertopurchaseGetCommunicationListV1ResponseMPayload

Response for GET /1/object/rejectedoffertopurchase/{pkiRejectedoffertopurchaseID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communication** | [**List[CustomCommunicationListElementResponse]**](CustomCommunicationListElementResponse.md) |  | 

## Example

```python
from eZmaxApi.models.rejectedoffertopurchase_get_communication_list_v1_response_m_payload import RejectedoffertopurchaseGetCommunicationListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RejectedoffertopurchaseGetCommunicationListV1ResponseMPayload from a JSON string
rejectedoffertopurchase_get_communication_list_v1_response_m_payload_instance = RejectedoffertopurchaseGetCommunicationListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(RejectedoffertopurchaseGetCommunicationListV1ResponseMPayload.to_json())

# convert the object into a dict
rejectedoffertopurchase_get_communication_list_v1_response_m_payload_dict = rejectedoffertopurchase_get_communication_list_v1_response_m_payload_instance.to_dict()
# create an instance of RejectedoffertopurchaseGetCommunicationListV1ResponseMPayload from a dict
rejectedoffertopurchase_get_communication_list_v1_response_m_payload_from_dict = RejectedoffertopurchaseGetCommunicationListV1ResponseMPayload.from_dict(rejectedoffertopurchase_get_communication_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


