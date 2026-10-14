# SupplierGetCommunicationsendersV1ResponseMPayload

Response for GET /1/object/supplier/{pkiSupplierID}/getCommunicationsenders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationsenders** | [**List[CustomCommunicationsenderResponse]**](CustomCommunicationsenderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.supplier_get_communicationsenders_v1_response_m_payload import SupplierGetCommunicationsendersV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierGetCommunicationsendersV1ResponseMPayload from a JSON string
supplier_get_communicationsenders_v1_response_m_payload_instance = SupplierGetCommunicationsendersV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SupplierGetCommunicationsendersV1ResponseMPayload.to_json())

# convert the object into a dict
supplier_get_communicationsenders_v1_response_m_payload_dict = supplier_get_communicationsenders_v1_response_m_payload_instance.to_dict()
# create an instance of SupplierGetCommunicationsendersV1ResponseMPayload from a dict
supplier_get_communicationsenders_v1_response_m_payload_from_dict = SupplierGetCommunicationsendersV1ResponseMPayload.from_dict(supplier_get_communicationsenders_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


