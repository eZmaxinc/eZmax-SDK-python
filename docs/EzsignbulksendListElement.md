# EzsignbulksendListElement

An Ezsignbulksend List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignbulksend_id** | **int** | The unique ID of the Ezsignbulksend | 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**s_ezsignbulksend_description** | **str** | The description of the Ezsignbulksend | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | 
**b_ezsignbulksend_needvalidation** | **bool** | Whether the Ezsigntemplatepackage was automatically modified and needs a manual validation | 
**i_ezsignbulksendtransmission** | **int** | The total number of Ezsignbulksendtransmissions in the Ezsignbulksend | 
**i_ezsignfolder** | **int** | The total number of Ezsignfolders in the Ezsignbulksend | 
**i_ezsigndocument** | **int** | The total number of Ezsigndocuments in the Ezsignbulksend | 
**i_ezsignsignature** | **int** | The total number of Ezsignsignature in the Ezsignbulksend | 
**i_ezsignsignature_signed** | **int** | The total number of already signed Ezsignsignature blocks in the Ezsignbulksend | 
**b_ezsignbulksend_isactive** | **bool** | Whether the Ezsignbulksend is active or not | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_list_element import EzsignbulksendListElement

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendListElement from a JSON string
ezsignbulksend_list_element_instance = EzsignbulksendListElement.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendListElement.to_json())

# convert the object into a dict
ezsignbulksend_list_element_dict = ezsignbulksend_list_element_instance.to_dict()
# create an instance of EzsignbulksendListElement from a dict
ezsignbulksend_list_element_form_dict = ezsignbulksend_list_element.from_dict(ezsignbulksend_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


