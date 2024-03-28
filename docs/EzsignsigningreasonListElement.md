# EzsignsigningreasonListElement

A Ezsignsigningreason List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignsigningreason_id** | **int** | The unique ID of the Ezsignsigningreason | 
**s_ezsignsigningreason_description_x** | **str** | The description of the Ezsignsigningreason in the language of the requester | 
**b_ezsignsigningreason_isactive** | **bool** | Whether the ezsignsigningreason is active or not | 

## Example

```python
from eZmaxApi.models.ezsignsigningreason_list_element import EzsignsigningreasonListElement

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsigningreasonListElement from a JSON string
ezsignsigningreason_list_element_instance = EzsignsigningreasonListElement.from_json(json)
# print the JSON string representation of the object
print(EzsignsigningreasonListElement.to_json())

# convert the object into a dict
ezsignsigningreason_list_element_dict = ezsignsigningreason_list_element_instance.to_dict()
# create an instance of EzsignsigningreasonListElement from a dict
ezsignsigningreason_list_element_form_dict = ezsignsigningreason_list_element.from_dict(ezsignsigningreason_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


