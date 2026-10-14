# SupplierGetCommunicationCountV1ResponseMPayload

Response for GET /1/object/supplier/{pkiSupplierID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_communication_count** | **int** | The count of Communication. | 

## Example

```python
from eZmaxApi.models.supplier_get_communication_count_v1_response_m_payload import SupplierGetCommunicationCountV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierGetCommunicationCountV1ResponseMPayload from a JSON string
supplier_get_communication_count_v1_response_m_payload_instance = SupplierGetCommunicationCountV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SupplierGetCommunicationCountV1ResponseMPayload.to_json())

# convert the object into a dict
supplier_get_communication_count_v1_response_m_payload_dict = supplier_get_communication_count_v1_response_m_payload_instance.to_dict()
# create an instance of SupplierGetCommunicationCountV1ResponseMPayload from a dict
supplier_get_communication_count_v1_response_m_payload_from_dict = SupplierGetCommunicationCountV1ResponseMPayload.from_dict(supplier_get_communication_count_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


