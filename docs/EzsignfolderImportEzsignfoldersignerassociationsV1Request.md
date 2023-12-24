# EzsignfolderImportEzsignfoldersignerassociationsV1Request

Request for POST /1/object/ezsignfolder/{pkiEzsignfolderID}/importEzsignfoldersignerassociations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_fki_ezsignfoldersignerassociation_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_import_ezsignfoldersignerassociations_v1_request import EzsignfolderImportEzsignfoldersignerassociationsV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderImportEzsignfoldersignerassociationsV1Request from a JSON string
ezsignfolder_import_ezsignfoldersignerassociations_v1_request_instance = EzsignfolderImportEzsignfoldersignerassociationsV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignfolderImportEzsignfoldersignerassociationsV1Request.to_json()

# convert the object into a dict
ezsignfolder_import_ezsignfoldersignerassociations_v1_request_dict = ezsignfolder_import_ezsignfoldersignerassociations_v1_request_instance.to_dict()
# create an instance of EzsignfolderImportEzsignfoldersignerassociationsV1Request from a dict
ezsignfolder_import_ezsignfoldersignerassociations_v1_request_form_dict = ezsignfolder_import_ezsignfoldersignerassociations_v1_request.from_dict(ezsignfolder_import_ezsignfoldersignerassociations_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


