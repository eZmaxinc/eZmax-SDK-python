# OtherincomeListElement

A Otherincome List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_otherincome_id** | **int** | The unique ID of the Otherincome | 
**fki_otherincometype_id** | **int** | The unique ID of the Otherincometype | 
**s_otherincometype_description_x** | **str** | The description of the Otherincometype in the language of the requester | 
**s_otherincome_description** | **str** | The description of the Otherincome | 
**e_otherincome_remunerationtype** | [**FieldEOtherincomeRemunerationtype**](FieldEOtherincomeRemunerationtype.md) |  | 
**d_otherincome_remunerationsubtotal** | **str** | The remuneration subtotal of the Otherincome | 
**d_otherincome_remunerationtaxes** | **str** | The remuneration total taxes of the Otherincome | [optional] 
**d_otherincome_remunerationtotal** | **str** | The remuneration total of the Otherincome | [optional] 
**dt_otherincome_paid** | **str** | The paid of the Otherincome | 
**b_otherincome_isactive** | **bool** | Whether the otherincome is active or not | 

## Example

```python
from eZmaxApi.models.otherincome_list_element import OtherincomeListElement

# TODO update the JSON string below
json = "{}"
# create an instance of OtherincomeListElement from a JSON string
otherincome_list_element_instance = OtherincomeListElement.from_json(json)
# print the JSON string representation of the object
print(OtherincomeListElement.to_json())

# convert the object into a dict
otherincome_list_element_dict = otherincome_list_element_instance.to_dict()
# create an instance of OtherincomeListElement from a dict
otherincome_list_element_from_dict = OtherincomeListElement.from_dict(otherincome_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


