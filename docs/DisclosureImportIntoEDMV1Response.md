# DisclosureImportIntoEDMV1Response

Response for POST /1/object/disclosure/{pkiDisclosureID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DisclosureImportIntoEDMV1ResponseMPayload**](DisclosureImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.disclosure_import_into_edmv1_response import DisclosureImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureImportIntoEDMV1Response from a JSON string
disclosure_import_into_edmv1_response_instance = DisclosureImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(DisclosureImportIntoEDMV1Response.to_json())

# convert the object into a dict
disclosure_import_into_edmv1_response_dict = disclosure_import_into_edmv1_response_instance.to_dict()
# create an instance of DisclosureImportIntoEDMV1Response from a dict
disclosure_import_into_edmv1_response_from_dict = DisclosureImportIntoEDMV1Response.from_dict(disclosure_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


