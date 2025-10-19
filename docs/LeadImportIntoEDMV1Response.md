# LeadImportIntoEDMV1Response

Request for POST /1/object/lead/{pkiLeadID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**LeadImportIntoEDMV1ResponseMPayload**](LeadImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.lead_import_into_edmv1_response import LeadImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of LeadImportIntoEDMV1Response from a JSON string
lead_import_into_edmv1_response_instance = LeadImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(LeadImportIntoEDMV1Response.to_json())

# convert the object into a dict
lead_import_into_edmv1_response_dict = lead_import_into_edmv1_response_instance.to_dict()
# create an instance of LeadImportIntoEDMV1Response from a dict
lead_import_into_edmv1_response_from_dict = LeadImportIntoEDMV1Response.from_dict(lead_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


