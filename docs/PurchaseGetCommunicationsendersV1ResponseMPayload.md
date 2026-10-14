# PurchaseGetCommunicationsendersV1ResponseMPayload

Response for GET /1/object/purchase/{pkiPurchaseID}/getCommunicationsenders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationsenders** | [**List[CustomCommunicationsenderResponse]**](CustomCommunicationsenderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.purchase_get_communicationsenders_v1_response_m_payload import PurchaseGetCommunicationsendersV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseGetCommunicationsendersV1ResponseMPayload from a JSON string
purchase_get_communicationsenders_v1_response_m_payload_instance = PurchaseGetCommunicationsendersV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PurchaseGetCommunicationsendersV1ResponseMPayload.to_json())

# convert the object into a dict
purchase_get_communicationsenders_v1_response_m_payload_dict = purchase_get_communicationsenders_v1_response_m_payload_instance.to_dict()
# create an instance of PurchaseGetCommunicationsendersV1ResponseMPayload from a dict
purchase_get_communicationsenders_v1_response_m_payload_from_dict = PurchaseGetCommunicationsendersV1ResponseMPayload.from_dict(purchase_get_communicationsenders_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


