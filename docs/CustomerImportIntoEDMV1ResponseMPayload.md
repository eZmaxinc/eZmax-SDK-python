# CustomerImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/customer/{pkiCustomerID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.customer_import_into_edmv1_response_m_payload import CustomerImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerImportIntoEDMV1ResponseMPayload from a JSON string
customer_import_into_edmv1_response_m_payload_instance = CustomerImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CustomerImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
customer_import_into_edmv1_response_m_payload_dict = customer_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of CustomerImportIntoEDMV1ResponseMPayload from a dict
customer_import_into_edmv1_response_m_payload_from_dict = CustomerImportIntoEDMV1ResponseMPayload.from_dict(customer_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


