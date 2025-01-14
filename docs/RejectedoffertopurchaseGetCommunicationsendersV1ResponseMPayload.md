# RejectedoffertopurchaseGetCommunicationsendersV1ResponseMPayload

Response for GET /1/object/rejectedoffertopurchase/{pkiRejectedoffertopurchaseID}/getCommunicationsenders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationsenders** | [**List[CustomCommunicationsenderResponse]**](CustomCommunicationsenderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.rejectedoffertopurchase_get_communicationsenders_v1_response_m_payload import RejectedoffertopurchaseGetCommunicationsendersV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RejectedoffertopurchaseGetCommunicationsendersV1ResponseMPayload from a JSON string
rejectedoffertopurchase_get_communicationsenders_v1_response_m_payload_instance = RejectedoffertopurchaseGetCommunicationsendersV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(RejectedoffertopurchaseGetCommunicationsendersV1ResponseMPayload.to_json())

# convert the object into a dict
rejectedoffertopurchase_get_communicationsenders_v1_response_m_payload_dict = rejectedoffertopurchase_get_communicationsenders_v1_response_m_payload_instance.to_dict()
# create an instance of RejectedoffertopurchaseGetCommunicationsendersV1ResponseMPayload from a dict
rejectedoffertopurchase_get_communicationsenders_v1_response_m_payload_from_dict = RejectedoffertopurchaseGetCommunicationsendersV1ResponseMPayload.from_dict(rejectedoffertopurchase_get_communicationsenders_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


