# EzsignfoldertypeListElement

An Ezsignfoldertype List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**e_ezsignfoldertype_privacylevel** | [**FieldEEzsignfoldertypePrivacylevel**](FieldEEzsignfoldertypePrivacylevel.md) |  | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | 
**b_ezsignfoldertype_isactive** | **bool** | Whether the Ezsignfoldertype is active or not | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_list_element import EzsignfoldertypeListElement

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeListElement from a JSON string
ezsignfoldertype_list_element_instance = EzsignfoldertypeListElement.from_json(json)
# print the JSON string representation of the object
print EzsignfoldertypeListElement.to_json()

# convert the object into a dict
ezsignfoldertype_list_element_dict = ezsignfoldertype_list_element_instance.to_dict()
# create an instance of EzsignfoldertypeListElement from a dict
ezsignfoldertype_list_element_form_dict = ezsignfoldertype_list_element.from_dict(ezsignfoldertype_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


