# LeadImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/lead/{pkiLeadID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.lead_import_into_edmv1_response_m_payload import LeadImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of LeadImportIntoEDMV1ResponseMPayload from a JSON string
lead_import_into_edmv1_response_m_payload_instance = LeadImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(LeadImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
lead_import_into_edmv1_response_m_payload_dict = lead_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of LeadImportIntoEDMV1ResponseMPayload from a dict
lead_import_into_edmv1_response_m_payload_from_dict = LeadImportIntoEDMV1ResponseMPayload.from_dict(lead_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


