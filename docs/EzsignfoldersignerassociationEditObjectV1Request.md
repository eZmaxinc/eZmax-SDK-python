# EzsignfoldersignerassociationEditObjectV1Request

Request for PUT /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfoldersignerassociation** | [**EzsignfoldersignerassociationRequestCompound**](EzsignfoldersignerassociationRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_edit_object_v1_request import EzsignfoldersignerassociationEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationEditObjectV1Request from a JSON string
ezsignfoldersignerassociation_edit_object_v1_request_instance = EzsignfoldersignerassociationEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationEditObjectV1Request.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_edit_object_v1_request_dict = ezsignfoldersignerassociation_edit_object_v1_request_instance.to_dict()
# create an instance of EzsignfoldersignerassociationEditObjectV1Request from a dict
ezsignfoldersignerassociation_edit_object_v1_request_form_dict = ezsignfoldersignerassociation_edit_object_v1_request.from_dict(ezsignfoldersignerassociation_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


