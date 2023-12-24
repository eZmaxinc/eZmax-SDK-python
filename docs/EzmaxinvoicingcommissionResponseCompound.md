# EzmaxinvoicingcommissionResponseCompound

A Ezmaxinvoicingcommission Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxinvoicingcommission_id** | **int** | The unique ID of the Ezmaxinvoicingcommission | [optional] 
**fki_ezmaxinvoicingsummaryglobal_id** | **int** | The unique ID of the Ezmaxinvoicingsummaryglobal | [optional] 
**fki_ezmaxpartner_id** | **int** | The unique ID of the Ezmaxpartner | [optional] 
**fki_ezmaxrepresentative_id** | **int** | The unique ID of the Ezmaxrepresentative | [optional] 
**dt_ezmaxinvoicingcommission_start** | **str** | The start date for the Ezmaxinvoicingcommission | 
**dt_ezmaxinvoicingcommission_end** | **str** | The end date for the Ezmaxinvoicingcommission | 
**i_ezmaxinvoicingcommission_days** | **int** | This is the number of days during the month on which the Ezmaxinvoigcommission applies | 
**d_ezmaxinvoicingcommission_amount** | **str** | The amount of Ezmaxinvoicingcommission | 
**obj_contact_name** | [**CustomContactNameResponse**](CustomContactNameResponse.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezmaxinvoicingcommission_response_compound import EzmaxinvoicingcommissionResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingcommissionResponseCompound from a JSON string
ezmaxinvoicingcommission_response_compound_instance = EzmaxinvoicingcommissionResponseCompound.from_json(json)
# print the JSON string representation of the object
print EzmaxinvoicingcommissionResponseCompound.to_json()

# convert the object into a dict
ezmaxinvoicingcommission_response_compound_dict = ezmaxinvoicingcommission_response_compound_instance.to_dict()
# create an instance of EzmaxinvoicingcommissionResponseCompound from a dict
ezmaxinvoicingcommission_response_compound_form_dict = ezmaxinvoicingcommission_response_compound.from_dict(ezmaxinvoicingcommission_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


