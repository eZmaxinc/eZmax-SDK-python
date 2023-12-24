# EzsignfolderImportEzsigntemplatepackageV1Response

Response for POST/1/object/ezsignfolder/{pkiEzsignfolderID}/importEzsigntemplatepackage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfolderImportEzsigntemplatepackageV1ResponseMPayload**](EzsignfolderImportEzsigntemplatepackageV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_import_ezsigntemplatepackage_v1_response import EzsignfolderImportEzsigntemplatepackageV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderImportEzsigntemplatepackageV1Response from a JSON string
ezsignfolder_import_ezsigntemplatepackage_v1_response_instance = EzsignfolderImportEzsigntemplatepackageV1Response.from_json(json)
# print the JSON string representation of the object
print EzsignfolderImportEzsigntemplatepackageV1Response.to_json()

# convert the object into a dict
ezsignfolder_import_ezsigntemplatepackage_v1_response_dict = ezsignfolder_import_ezsigntemplatepackage_v1_response_instance.to_dict()
# create an instance of EzsignfolderImportEzsigntemplatepackageV1Response from a dict
ezsignfolder_import_ezsigntemplatepackage_v1_response_form_dict = ezsignfolder_import_ezsigntemplatepackage_v1_response.from_dict(ezsignfolder_import_ezsigntemplatepackage_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


