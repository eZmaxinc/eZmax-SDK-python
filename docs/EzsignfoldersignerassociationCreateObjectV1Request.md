# EzsignfoldersignerassociationCreateObjectV1Request

Request for POST /1/object/ezsignfoldersignerassociation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfoldersignerassociation** | [**EzsignfoldersignerassociationRequest**](EzsignfoldersignerassociationRequest.md) |  | [optional] 
**obj_ezsignfoldersignerassociation_compound** | [**EzsignfoldersignerassociationRequestCompound**](EzsignfoldersignerassociationRequestCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_create_object_v1_request import EzsignfoldersignerassociationCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationCreateObjectV1Request from a JSON string
ezsignfoldersignerassociation_create_object_v1_request_instance = EzsignfoldersignerassociationCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignfoldersignerassociationCreateObjectV1Request.to_json()

# convert the object into a dict
ezsignfoldersignerassociation_create_object_v1_request_dict = ezsignfoldersignerassociation_create_object_v1_request_instance.to_dict()
# create an instance of EzsignfoldersignerassociationCreateObjectV1Request from a dict
ezsignfoldersignerassociation_create_object_v1_request_form_dict = ezsignfoldersignerassociation_create_object_v1_request.from_dict(ezsignfoldersignerassociation_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


