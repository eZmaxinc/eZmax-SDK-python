# LeadImportIntoEDMV1Request

Request for POST /1/object/lead/{pkiLeadID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.lead_import_into_edmv1_request import LeadImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of LeadImportIntoEDMV1Request from a JSON string
lead_import_into_edmv1_request_instance = LeadImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(LeadImportIntoEDMV1Request.to_json())

# convert the object into a dict
lead_import_into_edmv1_request_dict = lead_import_into_edmv1_request_instance.to_dict()
# create an instance of LeadImportIntoEDMV1Request from a dict
lead_import_into_edmv1_request_from_dict = LeadImportIntoEDMV1Request.from_dict(lead_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


