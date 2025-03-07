# EzsignimportfolderListElement

A Ezsignimportfolder List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignimportfolder_id** | **int** | The unique ID of the Ezsignimportfolder | 
**s_ezsignimportfolder_name** | **str** | The name of the Ezsignimportfolder | 
**dt_created_date** | **str** | The date and time at which the object was created | [optional] 
**dt_modified_date** | **str** | The date and time at which the object was last modified | [optional] 
**i_total_ezsignimportdocument** | **int** | The count of Ezsignimportdocument. | [optional] 
**i_total_ezsignimportdocument_not_imported** | **int** | The count of Ezsignimportdocument not imported in an Ezsignfolder. | [optional] 
**e_ezsignimportfolder_status** | [**ComputedEEzsignimportfolderStatus**](ComputedEEzsignimportfolderStatus.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignimportfolder_list_element import EzsignimportfolderListElement

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignimportfolderListElement from a JSON string
ezsignimportfolder_list_element_instance = EzsignimportfolderListElement.from_json(json)
# print the JSON string representation of the object
print(EzsignimportfolderListElement.to_json())

# convert the object into a dict
ezsignimportfolder_list_element_dict = ezsignimportfolder_list_element_instance.to_dict()
# create an instance of EzsignimportfolderListElement from a dict
ezsignimportfolder_list_element_from_dict = EzsignimportfolderListElement.from_dict(ezsignimportfolder_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


