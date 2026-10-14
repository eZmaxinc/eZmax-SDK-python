# SupplierGetCommunicationListV1ResponseMPayload

Response for GET /1/object/supplier/{pkiSupplierID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communication** | [**List[CustomCommunicationListElementResponse]**](CustomCommunicationListElementResponse.md) |  | 

## Example

```python
from eZmaxApi.models.supplier_get_communication_list_v1_response_m_payload import SupplierGetCommunicationListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierGetCommunicationListV1ResponseMPayload from a JSON string
supplier_get_communication_list_v1_response_m_payload_instance = SupplierGetCommunicationListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SupplierGetCommunicationListV1ResponseMPayload.to_json())

# convert the object into a dict
supplier_get_communication_list_v1_response_m_payload_dict = supplier_get_communication_list_v1_response_m_payload_instance.to_dict()
# create an instance of SupplierGetCommunicationListV1ResponseMPayload from a dict
supplier_get_communication_list_v1_response_m_payload_from_dict = SupplierGetCommunicationListV1ResponseMPayload.from_dict(supplier_get_communication_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


