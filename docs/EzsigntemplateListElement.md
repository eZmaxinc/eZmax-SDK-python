# EzsigntemplateListElement

A Ezsigntemplate List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | [optional] 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_ezsigntemplate_description** | **str** | The description of the Ezsigntemplate | 
**i_ezsigntemplatedocument_pagetotal** | **int** | The number of pages in the Ezsigntemplatedocument. | [optional] 
**i_ezsigntemplate_signaturetotal** | **int** | The number of total signatures in the Ezsigntemplate. | [optional] 
**i_ezsigntemplate_formfieldtotal** | **int** | The number of total form fields in the Ezsigntemplate. | [optional] 
**b_ezsigntemplate_incomplete** | **bool** | Indicate the Ezsigntemplate is incomplete and cannot be used | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | [optional] 
**e_ezsigntemplate_type** | [**FieldEEzsigntemplateType**](FieldEEzsigntemplateType.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_list_element import EzsigntemplateListElement

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateListElement from a JSON string
ezsigntemplate_list_element_instance = EzsigntemplateListElement.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateListElement.to_json())

# convert the object into a dict
ezsigntemplate_list_element_dict = ezsigntemplate_list_element_instance.to_dict()
# create an instance of EzsigntemplateListElement from a dict
ezsigntemplate_list_element_from_dict = EzsigntemplateListElement.from_dict(ezsigntemplate_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


