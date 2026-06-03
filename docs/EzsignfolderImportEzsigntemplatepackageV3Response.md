# EzsignfolderImportEzsigntemplatepackageV3Response

Response for POST/3/object/ezsignfolder/{pkiEzsignfolderID}/importEzsigntemplatepackage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfolderImportEzsigntemplatepackageV3ResponseMPayload**](EzsignfolderImportEzsigntemplatepackageV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_import_ezsigntemplatepackage_v3_response import EzsignfolderImportEzsigntemplatepackageV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderImportEzsigntemplatepackageV3Response from a JSON string
ezsignfolder_import_ezsigntemplatepackage_v3_response_instance = EzsignfolderImportEzsigntemplatepackageV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderImportEzsigntemplatepackageV3Response.to_json())

# convert the object into a dict
ezsignfolder_import_ezsigntemplatepackage_v3_response_dict = ezsignfolder_import_ezsigntemplatepackage_v3_response_instance.to_dict()
# create an instance of EzsignfolderImportEzsigntemplatepackageV3Response from a dict
ezsignfolder_import_ezsigntemplatepackage_v3_response_from_dict = EzsignfolderImportEzsigntemplatepackageV3Response.from_dict(ezsignfolder_import_ezsigntemplatepackage_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


