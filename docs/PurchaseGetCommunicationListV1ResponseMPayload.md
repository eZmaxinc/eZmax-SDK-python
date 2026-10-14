# PurchaseGetCommunicationListV1ResponseMPayload

Response for GET /1/object/purchase/{pkiPurchaseID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communication** | [**List[CustomCommunicationListElementResponse]**](CustomCommunicationListElementResponse.md) |  | 

## Example

```python
from eZmaxApi.models.purchase_get_communication_list_v1_response_m_payload import PurchaseGetCommunicationListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseGetCommunicationListV1ResponseMPayload from a JSON string
purchase_get_communication_list_v1_response_m_payload_instance = PurchaseGetCommunicationListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PurchaseGetCommunicationListV1ResponseMPayload.to_json())

# convert the object into a dict
purchase_get_communication_list_v1_response_m_payload_dict = purchase_get_communication_list_v1_response_m_payload_instance.to_dict()
# create an instance of PurchaseGetCommunicationListV1ResponseMPayload from a dict
purchase_get_communication_list_v1_response_m_payload_from_dict = PurchaseGetCommunicationListV1ResponseMPayload.from_dict(purchase_get_communication_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


