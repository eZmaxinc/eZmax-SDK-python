# EzsignfolderImportEzsigntemplatepackageV1ResponseMPayload

Payload for POST /1/object/ezsignfolder/{pkiEzsignfolderID}/importEzsigntemplatepackage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigndocument** | [**List[EzsigndocumentResponseCompound]**](EzsigndocumentResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_import_ezsigntemplatepackage_v1_response_m_payload import EzsignfolderImportEzsigntemplatepackageV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderImportEzsigntemplatepackageV1ResponseMPayload from a JSON string
ezsignfolder_import_ezsigntemplatepackage_v1_response_m_payload_instance = EzsignfolderImportEzsigntemplatepackageV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderImportEzsigntemplatepackageV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignfolder_import_ezsigntemplatepackage_v1_response_m_payload_dict = ezsignfolder_import_ezsigntemplatepackage_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderImportEzsigntemplatepackageV1ResponseMPayload from a dict
ezsignfolder_import_ezsigntemplatepackage_v1_response_m_payload_form_dict = ezsignfolder_import_ezsigntemplatepackage_v1_response_m_payload.from_dict(ezsignfolder_import_ezsigntemplatepackage_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


