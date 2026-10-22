# DocumenttypechecklistListElement

A Documenttypechecklist List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_documenttypechecklist_id** | **int** | The unique ID of the Documenttypechecklist | 
**fki_documenttype_id** | **int** | The unique ID of the Documenttype | 
**e_documenttypechecklist_status** | [**FieldEDocumenttypechecklistStatus**](FieldEDocumenttypechecklistStatus.md) |  | 
**t_documenttypechecklist_comment** | **str** | The comment of the Documenttypechecklist | 

## Example

```python
from eZmaxApi.models.documenttypechecklist_list_element import DocumenttypechecklistListElement

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypechecklistListElement from a JSON string
documenttypechecklist_list_element_instance = DocumenttypechecklistListElement.from_json(json)
# print the JSON string representation of the object
print(DocumenttypechecklistListElement.to_json())

# convert the object into a dict
documenttypechecklist_list_element_dict = documenttypechecklist_list_element_instance.to_dict()
# create an instance of DocumenttypechecklistListElement from a dict
documenttypechecklist_list_element_from_dict = DocumenttypechecklistListElement.from_dict(documenttypechecklist_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


