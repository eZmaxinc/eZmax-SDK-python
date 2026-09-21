# DisclosureListElement

A Disclosure List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_disclosure_id** | **int** | The unique ID of the Disclosure | 
**fki_agent_id** | **int** | The unique ID of the Agent. | [optional] 
**fki_broker_id** | **int** | The unique ID of the Broker. | [optional] 
**e_disclosure_interesttype** | [**FieldEDisclosureInteresttype**](FieldEDisclosureInteresttype.md) |  | 
**s_disclosure_relation** | **str** | The relation of the Disclosure | 
**dt_disclosure_redactiondate** | **str** | The redactiondate of the Disclosure | 
**dt_disclosure_acceptationdate** | **str** | The acceptationdate of the Disclosure | 
**dt_disclosure_receptiondate** | **str** | The receptiondate of the Disclosure | 
**b_disclosure_isactive** | **bool** | Whether the disclosure is active or not | 
**s_disclosure_number** | **str** | The number of a Disclosure | [optional] 
**s_contact_firstname** | **str** | The First name of the contact | [optional] 
**s_contact_lastname** | **str** | The Last name of the contact | [optional] 
**s_broker_name** | **str** | The name of the Broker | [optional] 

## Example

```python
from eZmaxApi.models.disclosure_list_element import DisclosureListElement

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureListElement from a JSON string
disclosure_list_element_instance = DisclosureListElement.from_json(json)
# print the JSON string representation of the object
print(DisclosureListElement.to_json())

# convert the object into a dict
disclosure_list_element_dict = disclosure_list_element_instance.to_dict()
# create an instance of DisclosureListElement from a dict
disclosure_list_element_from_dict = DisclosureListElement.from_dict(disclosure_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


