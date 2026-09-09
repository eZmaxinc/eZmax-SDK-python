# CommissionadvanceImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/commissionadvance/{pkiCommissionadvanceID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.commissionadvance_import_into_edmv1_response_m_payload import CommissionadvanceImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionadvanceImportIntoEDMV1ResponseMPayload from a JSON string
commissionadvance_import_into_edmv1_response_m_payload_instance = CommissionadvanceImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CommissionadvanceImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
commissionadvance_import_into_edmv1_response_m_payload_dict = commissionadvance_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of CommissionadvanceImportIntoEDMV1ResponseMPayload from a dict
commissionadvance_import_into_edmv1_response_m_payload_from_dict = CommissionadvanceImportIntoEDMV1ResponseMPayload.from_dict(commissionadvance_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


