# EzsignfoldersignerassociationReassignV1Request

Request for POST /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}/reassign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_reassign_v1_request import EzsignfoldersignerassociationReassignV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationReassignV1Request from a JSON string
ezsignfoldersignerassociation_reassign_v1_request_instance = EzsignfoldersignerassociationReassignV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationReassignV1Request.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_reassign_v1_request_dict = ezsignfoldersignerassociation_reassign_v1_request_instance.to_dict()
# create an instance of EzsignfoldersignerassociationReassignV1Request from a dict
ezsignfoldersignerassociation_reassign_v1_request_from_dict = EzsignfoldersignerassociationReassignV1Request.from_dict(ezsignfoldersignerassociation_reassign_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


