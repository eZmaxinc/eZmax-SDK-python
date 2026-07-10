# EzsignfoldersignerassociationCreateObjectV3Request

Request for POST /2/object/ezsignfoldersignerassociation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignfoldersignerassociation** | [**List[EzsignfoldersignerassociationRequestCompoundV2]**](EzsignfoldersignerassociationRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_create_object_v3_request import EzsignfoldersignerassociationCreateObjectV3Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationCreateObjectV3Request from a JSON string
ezsignfoldersignerassociation_create_object_v3_request_instance = EzsignfoldersignerassociationCreateObjectV3Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationCreateObjectV3Request.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_create_object_v3_request_dict = ezsignfoldersignerassociation_create_object_v3_request_instance.to_dict()
# create an instance of EzsignfoldersignerassociationCreateObjectV3Request from a dict
ezsignfoldersignerassociation_create_object_v3_request_from_dict = EzsignfoldersignerassociationCreateObjectV3Request.from_dict(ezsignfoldersignerassociation_create_object_v3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


