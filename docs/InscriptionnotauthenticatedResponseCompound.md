# InscriptionnotauthenticatedResponseCompound

A Inscriptionnotauthenticated Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_inscriptionnotauthenticated_id** | **int** | The unique ID of the Inscriptionnotauthenticated. | 
**fki_inscription_id** | **int** | The unique ID of the Inscription. | 
**fki_department_id** | **int** | The unique ID of the Department | [optional] 
**s_department_name_x** | **str** | The Name of the Department in the language of the requester | [optional] 
**fki_financialinstitution_id** | **int** | The unique ID of the Financialinstitution | [optional] 
**s_financialinstitution_name_x** | **str** | The name of the Financialinstitution in the language of the requester | [optional] 
**fki_buyercontract_id** | **int** | The unique ID of the Buyercontract | [optional] 
**s_buyercontract_contract** | **str** | The number of the Buyercontract | [optional] 
**fki_mortgagesupplier_id** | **int** | The unique ID of the Mortgagesupplier | [optional] 
**s_mortgagesupplier_name_x** | **str** | The name of the Mortagesupplier in the language of the requester | [optional] 
**fki_taxassignment_id** | **int** | The unique ID of the Taxassignment.  Valid values:  |Value|Description| |-|-| |1|No tax| |2|GST| |3|HST (ON)| |4|HST (NB)| |5|HST (NS)| |6|HST (NL)| |7|HST (PE)| |8|GST + QST (QC)| |9|GST + QST (QC) Non-Recoverable| |10|GST + PST (BC)| |11|GST + PST (SK)| |12|GST + RST (MB)| |13|GST + PST (BC) Non-Recoverable| |14|GST + PST (SK) Non-Recoverable| |15|GST + RST (MB) Non-Recoverable| | 
**s_taxassignment_description_x** | **str** | The description of the Taxassignment  in the language of the requester | [optional] 
**dt_inscriptionnotauthenticated_transactiondate** | **str** | The transaction date of the Inscriptionnotauthenticated | [optional] 
**dt_inscriptionnotauthenticated_transactiondate_real** | **str** | The real transactiondate of the Inscriptionnotauthenticated | [optional] 
**dt_inscriptionnotauthenticated_depositdate** | **str** | The deposit date of the Inscriptionnotauthenticated | [optional] 
**e_inscriptionnotauthenticated_type** | [**FieldEInscriptionnotauthenticatedType**](FieldEInscriptionnotauthenticatedType.md) |  | 
**d_inscriptionnotauthenticated_mortgageloan** | **str** | The amount of the mortgage loan of the Inscriptionnotauthenticated | 
**et_inscriptionnotauthenticated_mortgagetype** | [**FieldEtInscriptionnotauthenticatedMortgagetype**](FieldEtInscriptionnotauthenticatedMortgagetype.md) |  | 
**d_inscriptionnotauthenticated_transactionprice** | **str** | The transaction price of the Inscriptionnotauthenticated | 
**e_inscriptionnotauthenticated_remunerationtype** | [**FieldEInscriptionnotauthenticatedRemunerationtype**](FieldEInscriptionnotauthenticatedRemunerationtype.md) |  | 
**d_inscriptionnotauthenticated_remuneration** | **str** | The amount for the remuneration of the Inscriptionnotauthenticated | 
**d_inscriptionnotauthenticated_remunerationsubtotal** | **str** | The subtotal for the remuneration of the Inscriptionnotauthenticated | 
**d_inscriptionnotauthenticated_remunerationtotal** | **str** | The total for the remuneration of the Inscriptionnotauthenticated | 
**dt_inscriptionnotauthenticated_cancellationdate** | **str** | The cancellation date of the Inscriptionnotauthenticated | [optional] 
**dt_inscriptionnotauthenticated_possessiondate** | **str** | The possession date of the Inscriptionnotauthenticated | [optional] 
**s_inscriptionnotauthenticated_offertopurchasenumber** | **str** | The offer to purchase number of the Inscriptionnotauthenticated | 
**dt_inscriptionnotauthenticated_notaryscheduledate** | **str** | The notary schedule date of the Inscriptionnotauthenticated | [optional] 
**dt_inscriptionnotauthenticated_financingscheduledate** | **str** | The financing schedule date of the Inscriptionnotauthenticated | [optional] 
**b_inscriptionnotauthenticated_conditional** | **bool** | Whether the inscriptionnotauthenticated is conditional | 
**b_inscriptionnotauthenticated_mortgageisreferenced** | **bool** | Whether if the mortgage is referenced | 
**b_inscriptionnotauthenticated_homeowner** | **bool** | Whether if it&#39;s an home owner | 
**t_inscriptionnotauthenticated_conditions** | **str** | The conditions of the Inscriptionnotauthenticated | 
**dt_inscriptionnotauthenticated_conditiondeadlinedate** | **str** | The condition deadline date of the Inscriptionnotauthenticated | [optional] 
**i_inscriptionnotauthenticated_order** | **int** | The order of the Inscriptionnotauthenticated | 
**b_inscriptionnotauthenticated_isactive** | **bool** | Whether the inscriptionnotauthenticated is active or not | 
**e_inscriptionnotauthenticated_residence_type** | [**FieldEInscriptionnotauthenticatedResidenceType**](FieldEInscriptionnotauthenticatedResidenceType.md) |  | 
**t_inscriptionnotauthenticated_checklistnote** | **str** | The checklist note of the Inscriptionnotauthenticated | 
**d_inscriptionnotauthenticated_selleronlyretribution** | **str** | The amount retribution for the seller only of the Inscriptionnotauthenticated | 
**b_inscriptionnotauthenticated_draft** | **bool** | Whether the Inscriptionnotauthenticated is a draft or not | 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_response_compound import InscriptionnotauthenticatedResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedResponseCompound from a JSON string
inscriptionnotauthenticated_response_compound_instance = InscriptionnotauthenticatedResponseCompound.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedResponseCompound.to_json())

# convert the object into a dict
inscriptionnotauthenticated_response_compound_dict = inscriptionnotauthenticated_response_compound_instance.to_dict()
# create an instance of InscriptionnotauthenticatedResponseCompound from a dict
inscriptionnotauthenticated_response_compound_from_dict = InscriptionnotauthenticatedResponseCompound.from_dict(inscriptionnotauthenticated_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


