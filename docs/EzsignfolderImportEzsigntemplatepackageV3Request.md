# EzsignfolderImportEzsigntemplatepackageV3Request

Request for POST /3/object/ezsignfolder/{pkiEzsignfolderID}/importEzsigntemplatepackage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**dt_ezsigndocument_duedate** | **str** | The maximum date and time at which the Ezsigndocument can be signed. | 
**a_obj_import_ezsigntemplatepackage_relation** | [**List[CustomImportEzsigntemplatepackageRelationRequest]**](CustomImportEzsigntemplatepackageRelationRequest.md) |  | 
**a_s_ezsigntemplateannotation_description** | **List[str]** |  | 
**a_s_ezsigntemplateannotation_defaulttext** | **List[str]** |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_import_ezsigntemplatepackage_v3_request import EzsignfolderImportEzsigntemplatepackageV3Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderImportEzsigntemplatepackageV3Request from a JSON string
ezsignfolder_import_ezsigntemplatepackage_v3_request_instance = EzsignfolderImportEzsigntemplatepackageV3Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderImportEzsigntemplatepackageV3Request.to_json())

# convert the object into a dict
ezsignfolder_import_ezsigntemplatepackage_v3_request_dict = ezsignfolder_import_ezsigntemplatepackage_v3_request_instance.to_dict()
# create an instance of EzsignfolderImportEzsigntemplatepackageV3Request from a dict
ezsignfolder_import_ezsigntemplatepackage_v3_request_from_dict = EzsignfolderImportEzsigntemplatepackageV3Request.from_dict(ezsignfolder_import_ezsigntemplatepackage_v3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


