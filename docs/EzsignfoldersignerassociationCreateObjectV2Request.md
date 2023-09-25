# EzsignfoldersignerassociationCreateObjectV2Request

Request for POST /2/object/ezsignfoldersignerassociation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignfoldersignerassociation** | [**List[EzsignfoldersignerassociationRequestCompound]**](EzsignfoldersignerassociationRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_create_object_v2_request import EzsignfoldersignerassociationCreateObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationCreateObjectV2Request from a JSON string
ezsignfoldersignerassociation_create_object_v2_request_instance = EzsignfoldersignerassociationCreateObjectV2Request.from_json(json)
# print the JSON string representation of the object
print EzsignfoldersignerassociationCreateObjectV2Request.to_json()

# convert the object into a dict
ezsignfoldersignerassociation_create_object_v2_request_dict = ezsignfoldersignerassociation_create_object_v2_request_instance.to_dict()
# create an instance of EzsignfoldersignerassociationCreateObjectV2Request from a dict
ezsignfoldersignerassociation_create_object_v2_request_form_dict = ezsignfoldersignerassociation_create_object_v2_request.from_dict(ezsignfoldersignerassociation_create_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


