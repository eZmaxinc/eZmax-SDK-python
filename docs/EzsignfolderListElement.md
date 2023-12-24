# EzsignfolderListElement

An Ezsignfolder List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**e_ezsignfoldertype_privacylevel** | [**FieldEEzsignfoldertypePrivacylevel**](FieldEEzsignfoldertypePrivacylevel.md) |  | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | 
**s_ezsignfolder_description** | **str** | The description of the Ezsignfolder | 
**e_ezsignfolder_step** | [**FieldEEzsignfolderStep**](FieldEEzsignfolderStep.md) |  | 
**dt_created_date** | **str** | The date and time at which the object was created | 
**dt_ezsignfolder_sentdate** | **str** | The date and time at which the Ezsignfolder was sent the last time. | [optional] 
**dt_ezsignfolder_duedate** | **str** | The maximum date and time at which the Ezsignfolder can be signed. | [optional] 
**i_ezsigndocument** | **int** | The total number of Ezsigndocument in the folder | 
**i_ezsigndocument_edm** | **int** | The total number of Ezsigndocument in the folder that were saved in the edm system | 
**i_ezsignsignature** | **int** | The total number of signature blocks in all Ezsigndocuments in the folder | 
**i_ezsignsignature_signed** | **int** | The total number of already signed signature blocks in all Ezsigndocuments in the folder | 

## Example

```python
from eZmaxApi.models.ezsignfolder_list_element import EzsignfolderListElement

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderListElement from a JSON string
ezsignfolder_list_element_instance = EzsignfolderListElement.from_json(json)
# print the JSON string representation of the object
print EzsignfolderListElement.to_json()

# convert the object into a dict
ezsignfolder_list_element_dict = ezsignfolder_list_element_instance.to_dict()
# create an instance of EzsignfolderListElement from a dict
ezsignfolder_list_element_form_dict = ezsignfolder_list_element.from_dict(ezsignfolder_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


