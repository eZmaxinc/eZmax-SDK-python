# EzsigntemplatepackageListElement

An Ezsigntemplatepackage List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_ezsigntemplatepackage_description** | **str** | The description of the Ezsigntemplatepackage | 
**b_ezsigntemplatepackage_needvalidation** | **bool** | Whether the Ezsignbulksend was automatically modified and needs a manual validation | 
**i_ezsigntemplatepackagemembership** | **int** | The total number of Ezsigntemplatepackagemembership in the Ezsigntemplatepackage | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | 
**b_ezsigntemplatepackage_isactive** | **bool** | Whether the Ezsigntemplatepackage is active or not | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_list_element import EzsigntemplatepackageListElement

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageListElement from a JSON string
ezsigntemplatepackage_list_element_instance = EzsigntemplatepackageListElement.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackageListElement.to_json()

# convert the object into a dict
ezsigntemplatepackage_list_element_dict = ezsigntemplatepackage_list_element_instance.to_dict()
# create an instance of EzsigntemplatepackageListElement from a dict
ezsigntemplatepackage_list_element_form_dict = ezsigntemplatepackage_list_element.from_dict(ezsigntemplatepackage_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


