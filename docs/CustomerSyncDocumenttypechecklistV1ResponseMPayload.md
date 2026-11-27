# CustomerSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/customer/{pkiCustomerID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.customer_sync_documenttypechecklist_v1_response_m_payload import CustomerSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
customer_sync_documenttypechecklist_v1_response_m_payload_instance = CustomerSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CustomerSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
customer_sync_documenttypechecklist_v1_response_m_payload_dict = customer_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of CustomerSyncDocumenttypechecklistV1ResponseMPayload from a dict
customer_sync_documenttypechecklist_v1_response_m_payload_from_dict = CustomerSyncDocumenttypechecklistV1ResponseMPayload.from_dict(customer_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


