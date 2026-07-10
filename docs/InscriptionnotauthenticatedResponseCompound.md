# InscriptionnotauthenticatedResponseCompound

A Inscriptionnotauthenticated Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_inscriptionnotauthenticated_id** | **int** | The unique ID of the Inscriptionnotauthenticated. | 
**fki_company_id** | **int** | The unique ID of the Company | 
**s_company_name_x** | **str** | The Name of the Company in the language of the requester | [optional] 
**fki_inscription_id** | **int** | The unique ID of the Inscription. | 
**fki_department_id** | **int** | The unique ID of the Department | 
**s_department_name_x** | **str** | The Name of the Department in the language of the requester | [optional] 
**fki_financialinstitution_id** | **int** | The unique ID of the Financialinstitution | 
**s_financialinstitution_name_x** | **str** | The name of the Financialinstitution in the language of the requester | [optional] 
**fki_buyercontract_id** | **int** | The unique ID of the Buyercontract | 
**s_buyercontract_contract** | **str** | The number of the Buyercontract | [optional] 
**fki_mortgagesupplier_id** | **int** | The unique ID of the Mortgagesupplier | 
**s_mortgagesupplier_name_x** | **str** | The name of the Mortagesupplier in the language of the requester | [optional] 
**fki_taxassignment_id** | **int** | The unique ID of the Taxassignment.  Valid values:  |Value|Description| |-|-| |1|No tax| |2|GST| |3|HST (ON)| |4|HST (NB)| |5|HST (NS)| |6|HST (NL)| |7|HST (PE)| |8|GST + QST (QC)| |9|GST + QST (QC) Non-Recoverable| |10|GST + PST (BC)| |11|GST + PST (SK)| |12|GST + RST (MB)| |13|GST + PST (BC) Non-Recoverable| |14|GST + PST (SK) Non-Recoverable| |15|GST + RST (MB) Non-Recoverable| | 
**s_taxassignment_description_x** | **str** | The description of the Taxassignment  in the language of the requester | [optional] 
**dt_inscriptionnotauthenticated_transactiondate** | **str** | The transactiondate of the Inscriptionnotauthenticated | 
**dt_inscriptionnotauthenticated_transactiondate_real** | **str** | The transactiondatereal of the Inscriptionnotauthenticated | 
**dt_inscriptionnotauthenticated_depositdate** | **str** | The depositdate of the Inscriptionnotauthenticated | 
**e_inscriptionnotauthenticated_type** | [**FieldEInscriptionnotauthenticatedType**](FieldEInscriptionnotauthenticatedType.md) |  | 
**d_inscriptionnotauthenticated_mortgageloan** | **str** | The mortgageloan of the Inscriptionnotauthenticated | 
**et_inscriptionnotauthenticated_mortgagetype** | [**FieldEtInscriptionnotauthenticatedMortgagetype**](FieldEtInscriptionnotauthenticatedMortgagetype.md) |  | 
**d_inscriptionnotauthenticated_transactionprice** | **str** | The transactionprice of the Inscriptionnotauthenticated | 
**e_inscriptionnotauthenticated_remunerationtype** | [**FieldEInscriptionnotauthenticatedRemunerationtype**](FieldEInscriptionnotauthenticatedRemunerationtype.md) |  | 
**d_inscriptionnotauthenticated_remuneration** | **str** | The remuneration of the Inscriptionnotauthenticated | 
**d_inscriptionnotauthenticated_remunerationsubtotal** | **str** | The remunerationsubtotal of the Inscriptionnotauthenticated | 
**d_inscriptionnotauthenticated_remunerationtotal** | **str** | The remunerationtotal of the Inscriptionnotauthenticated | 
**dt_inscriptionnotauthenticated_cancellationdate** | **str** | The cancellationdate of the Inscriptionnotauthenticated | 
**dt_inscriptionnotauthenticated_possessiondate** | **str** | The possessiondate of the Inscriptionnotauthenticated | 
**s_inscriptionnotauthenticated_offertopurchasenumber** | **str** | The Offer to purchase number | 
**dt_inscriptionnotauthenticated_notaryscheduledate** | **str** | The notaryscheduledate of the Inscriptionnotauthenticated | 
**dt_inscriptionnotauthenticated_financingscheduledate** | **str** | The financingscheduledate of the Inscriptionnotauthenticated | 
**b_inscriptionnotauthenticated_conditional** | **bool** | Whether the inscriptionnotauthenticated is conditional | 
**b_inscriptionnotauthenticated_mortgageisreferenced** | **bool** | Whether if it&#39;s an mortgageisreferenced | 
**b_inscriptionnotauthenticated_homeowner** | **bool** | Whether if it&#39;s an homeowner | 
**t_inscriptionnotauthenticated_conditions** | **str** | The conditions of the Inscriptionnotauthenticated | 
**dt_inscriptionnotauthenticated_conditiondeadlinedate** | **str** | The conditiondeadlinedate of the Inscriptionnotauthenticated | 
**i_inscriptionnotauthenticated_order** | **int** | The order of the Inscriptionnotauthenticated | 
**b_inscriptionnotauthenticated_isactive** | **bool** | Whether the inscriptionnotauthenticated is active or not | 
**e_inscriptionnotauthenticated_residence_type** | [**FieldEInscriptionnotauthenticatedResidenceType**](FieldEInscriptionnotauthenticatedResidenceType.md) |  | 
**t_inscriptionnotauthenticated_checklistnote** | **str** | The checklistnote of the Inscriptionnotauthenticated | 
**d_inscriptionnotauthenticated_selleronlyretribution** | **str** | The selleronlyretribution of the Inscriptionnotauthenticated | 
**b_inscriptionnotauthenticated_draft** | **bool** | Whether the inscriptionnotauthenticated is a draft or not | 

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


