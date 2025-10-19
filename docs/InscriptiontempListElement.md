# InscriptiontempListElement

A Inscriptiontemp List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_inscriptiontemp_id** | **int** | The unique ID of the Inscriptiontemp | 
**e_inscriptiontemp_status** | [**FieldEInscriptiontempStatus**](FieldEInscriptiontempStatus.md) |  | 
**s_inscriptiontemp_mls** | **str** | The mls of the Inscriptiontemp | [optional] 
**s_inscriptiontemp_description** | **str** | The description of the Inscriptiontemp | 
**b_inscriptiontemp_isactive** | **bool** | Whether the inscriptiontemp is active or not | 
**dt_created_date** | **str** | The date and time at which the object was created | 
**dt_modified_date** | **str** | The date and time at which the object was last modified | 

## Example

```python
from eZmaxApi.models.inscriptiontemp_list_element import InscriptiontempListElement

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptiontempListElement from a JSON string
inscriptiontemp_list_element_instance = InscriptiontempListElement.from_json(json)
# print the JSON string representation of the object
print(InscriptiontempListElement.to_json())

# convert the object into a dict
inscriptiontemp_list_element_dict = inscriptiontemp_list_element_instance.to_dict()
# create an instance of InscriptiontempListElement from a dict
inscriptiontemp_list_element_from_dict = InscriptiontempListElement.from_dict(inscriptiontemp_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


