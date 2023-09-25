# EzmaxinvoicingagentResponse

A Ezmaxinvoicingagent Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxinvoicingagent_id** | **int** | The unique ID of the Ezmaxinvoicingagent | [optional] 
**fki_ezmaxinvoicing_id** | **int** | The unique ID of the Ezmaxinvoicing | [optional] 
**fki_billingentityinternal_id** | **int** | The unique ID of the Billingentityinternal. | 
**s_billingentityinternal_description_x** | **str** | The description of the Billingentityinternal in the language of the requester | 
**fki_agent_id** | **int** | The unique ID of the Agent. | [optional] 
**fki_broker_id** | **int** | The unique ID of the Broker. | [optional] 
**i_ezmaxinvoicingagent_session** | **int** | The number of sessions | 
**i_ezmaxinvoicingagent_cloned** | **int** | The number of times this user was cloned | 
**i_ezmaxinvoicingagent_invoice** | **int** | The number of invoices | 
**i_ezmaxinvoicingagent_inscription** | **int** | The number of inscriptions | 
**i_ezmaxinvoicingagent_inscriptionactive** | **int** | The number of active inscriptions | 
**i_ezmaxinvoicingagent_sale** | **int** | The number of sales | 
**i_ezmaxinvoicingagent_otherincome** | **int** | The number of otherincomes | 
**i_ezmaxinvoicingagent_commissioncalculation** | **int** | The number of commission calculations | 
**i_ezmaxinvoicingagent_ezsigndocument** | **int** | The number of ezsign documents | 
**b_ezmaxinvoicingagent_ezsignaccount** | **bool** | Whether the agent has an eZsign account | 
**b_ezmaxinvoicingagent_billableezmax** | **bool** | Whether it is billable for eZmax | 
**e_ezmaxinvoicingagent_variationezmax** | [**FieldEEzmaxinvoicingagentVariationezmax**](FieldEEzmaxinvoicingagentVariationezmax.md) |  | 
**b_ezmaxinvoicingagent_billableezsign** | **bool** | Whether it is billable for eZsign | 
**e_ezmaxinvoicingagent_variationezsign** | [**FieldEEzmaxinvoicingagentVariationezsign**](FieldEEzmaxinvoicingagentVariationezsign.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxinvoicingagent_response import EzmaxinvoicingagentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingagentResponse from a JSON string
ezmaxinvoicingagent_response_instance = EzmaxinvoicingagentResponse.from_json(json)
# print the JSON string representation of the object
print EzmaxinvoicingagentResponse.to_json()

# convert the object into a dict
ezmaxinvoicingagent_response_dict = ezmaxinvoicingagent_response_instance.to_dict()
# create an instance of EzmaxinvoicingagentResponse from a dict
ezmaxinvoicingagent_response_form_dict = ezmaxinvoicingagent_response.from_dict(ezmaxinvoicingagent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


