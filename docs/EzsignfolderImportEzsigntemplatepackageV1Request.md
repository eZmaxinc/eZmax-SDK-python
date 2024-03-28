# EzsignfolderImportEzsigntemplatepackageV1Request

Request for POST /1/object/ezsignfolder/{pkiEzsignfolderID}/importEzsigntemplatepackage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**dt_ezsigndocument_duedate** | **str** | The maximum date and time at which the Ezsigndocument can be signed. | 
**a_obj_import_ezsigntemplatepackage_relation** | [**List[CustomImportEzsigntemplatepackageRelationRequest]**](CustomImportEzsigntemplatepackageRelationRequest.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_import_ezsigntemplatepackage_v1_request import EzsignfolderImportEzsigntemplatepackageV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderImportEzsigntemplatepackageV1Request from a JSON string
ezsignfolder_import_ezsigntemplatepackage_v1_request_instance = EzsignfolderImportEzsigntemplatepackageV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderImportEzsigntemplatepackageV1Request.to_json())

# convert the object into a dict
ezsignfolder_import_ezsigntemplatepackage_v1_request_dict = ezsignfolder_import_ezsigntemplatepackage_v1_request_instance.to_dict()
# create an instance of EzsignfolderImportEzsigntemplatepackageV1Request from a dict
ezsignfolder_import_ezsigntemplatepackage_v1_request_form_dict = ezsignfolder_import_ezsigntemplatepackage_v1_request.from_dict(ezsignfolder_import_ezsigntemplatepackage_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


