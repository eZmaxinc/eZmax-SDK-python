# LeadListElement

A Lead List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_lead_id** | **int** | The unique ID of the Lead | 
**fki_leadsource_id** | **int** | The unique ID of the Leadsource | 
**s_leadsource_name_x** | **str** | The name of the Leadsource in the language of the requester | 
**e_lead_status** | [**FieldELeadStatus**](FieldELeadStatus.md) |  | 
**dt_lead_expiration** | **str** | The expiration of the Lead | 
**b_lead_isactive** | **bool** | Whether the lead is active or not | 
**s_lead_code** | **str** | The code of the Lead | 

## Example

```python
from eZmaxApi.models.lead_list_element import LeadListElement

# TODO update the JSON string below
json = "{}"
# create an instance of LeadListElement from a JSON string
lead_list_element_instance = LeadListElement.from_json(json)
# print the JSON string representation of the object
print(LeadListElement.to_json())

# convert the object into a dict
lead_list_element_dict = lead_list_element_instance.to_dict()
# create an instance of LeadListElement from a dict
lead_list_element_from_dict = LeadListElement.from_dict(lead_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


