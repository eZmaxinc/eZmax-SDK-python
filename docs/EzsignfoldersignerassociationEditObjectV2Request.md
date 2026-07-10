# EzsignfoldersignerassociationEditObjectV2Request

Request for PUT /2/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfoldersignerassociation** | [**EzsignfoldersignerassociationRequestCompoundV2**](EzsignfoldersignerassociationRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_edit_object_v2_request import EzsignfoldersignerassociationEditObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationEditObjectV2Request from a JSON string
ezsignfoldersignerassociation_edit_object_v2_request_instance = EzsignfoldersignerassociationEditObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationEditObjectV2Request.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_edit_object_v2_request_dict = ezsignfoldersignerassociation_edit_object_v2_request_instance.to_dict()
# create an instance of EzsignfoldersignerassociationEditObjectV2Request from a dict
ezsignfoldersignerassociation_edit_object_v2_request_from_dict = EzsignfoldersignerassociationEditObjectV2Request.from_dict(ezsignfoldersignerassociation_edit_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


