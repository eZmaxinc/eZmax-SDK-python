# EzsignfolderImportEzsigntemplatepackageV2ResponseMPayload

Payload for POST /2/object/ezsignfolder/{pkiEzsignfolderID}/importEzsigntemplatepackage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigndocument** | [**List[EzsigndocumentResponseCompoundV3]**](EzsigndocumentResponseCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_import_ezsigntemplatepackage_v2_response_m_payload import EzsignfolderImportEzsigntemplatepackageV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderImportEzsigntemplatepackageV2ResponseMPayload from a JSON string
ezsignfolder_import_ezsigntemplatepackage_v2_response_m_payload_instance = EzsignfolderImportEzsigntemplatepackageV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderImportEzsigntemplatepackageV2ResponseMPayload.to_json())

# convert the object into a dict
ezsignfolder_import_ezsigntemplatepackage_v2_response_m_payload_dict = ezsignfolder_import_ezsigntemplatepackage_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderImportEzsigntemplatepackageV2ResponseMPayload from a dict
ezsignfolder_import_ezsigntemplatepackage_v2_response_m_payload_from_dict = EzsignfolderImportEzsigntemplatepackageV2ResponseMPayload.from_dict(ezsignfolder_import_ezsigntemplatepackage_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


