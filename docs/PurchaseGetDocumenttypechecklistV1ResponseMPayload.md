# PurchaseGetDocumenttypechecklistV1ResponseMPayload

Response for GET /1/object/purchase/{pkiPurchaseID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.purchase_get_documenttypechecklist_v1_response_m_payload import PurchaseGetDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseGetDocumenttypechecklistV1ResponseMPayload from a JSON string
purchase_get_documenttypechecklist_v1_response_m_payload_instance = PurchaseGetDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PurchaseGetDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
purchase_get_documenttypechecklist_v1_response_m_payload_dict = purchase_get_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of PurchaseGetDocumenttypechecklistV1ResponseMPayload from a dict
purchase_get_documenttypechecklist_v1_response_m_payload_from_dict = PurchaseGetDocumenttypechecklistV1ResponseMPayload.from_dict(purchase_get_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


