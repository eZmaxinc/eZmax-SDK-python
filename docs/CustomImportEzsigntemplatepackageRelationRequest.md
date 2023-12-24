# CustomImportEzsigntemplatepackageRelationRequest

The object used in /1/object/ezsignfolder/{pkiEzsignfolderID}/importEzsigntemplatepackage Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsigntemplatepackagesigner_id** | **int** | The unique ID of the Ezsigntemplatepackagesigner | [optional] 
**fki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | 
**s_ezsigntemplatepackagesigner_description** | **str** | The description of the Ezsigntemplatepackagesigner | [optional] 

## Example

```python
from eZmaxApi.models.custom_import_ezsigntemplatepackage_relation_request import CustomImportEzsigntemplatepackageRelationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomImportEzsigntemplatepackageRelationRequest from a JSON string
custom_import_ezsigntemplatepackage_relation_request_instance = CustomImportEzsigntemplatepackageRelationRequest.from_json(json)
# print the JSON string representation of the object
print CustomImportEzsigntemplatepackageRelationRequest.to_json()

# convert the object into a dict
custom_import_ezsigntemplatepackage_relation_request_dict = custom_import_ezsigntemplatepackage_relation_request_instance.to_dict()
# create an instance of CustomImportEzsigntemplatepackageRelationRequest from a dict
custom_import_ezsigntemplatepackage_relation_request_form_dict = custom_import_ezsigntemplatepackage_relation_request.from_dict(custom_import_ezsigntemplatepackage_relation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


