# InscriptionResponseCompound

A Inscription Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_inscription_id** | **int** | The unique ID of the Inscription. | 
**fki_department_id** | **int** | The unique ID of the Department | [optional] 
**s_department_name_x** | **str** | The Name of the Department in the language of the requester | [optional] 
**fki_realestateboard_id** | **int** | The unique ID of the Realestateboard | 
**s_realestateboard_name_x** | **str** | The name of the Realestateboard | [optional] 
**fki_address_id** | **int** | The unique ID of the Address | 
**obj_address** | [**AddressResponseCompound**](AddressResponseCompound.md) |  | [optional] 
**fki_inscriptionbuildingtype_id** | **int** | The unique ID of the Inscriptionbuildingtype | 
**s_inscriptionbuildingtype_name_x** | **str** | The name of the Inscriptionbuildingtype in the language of the requester | [optional] 
**fki_inscriptiontype_id** | **int** | The unique ID of the Inscriptiontype | 
**s_inscriptiontype_name_x** | **str** | The name of the Inscriptiontype in the language of the requester | [optional] 
**fki_inscriptioncategory_id** | **int** | The unique ID of the Inscriptioncategory | 
**s_inscriptioncategory_name_x** | **str** | The name of the Inscriptioncategory in the language of the requester | [optional] 
**e_inscription_step** | [**FieldEInscriptionStep**](FieldEInscriptionStep.md) |  | 
**e_inscription_residence_type** | [**FieldEInscriptionResidenceType**](FieldEInscriptionResidenceType.md) |  | 
**s_inscription_civicend** | **str** | The address civic end of the Inscription | 
**s_inscription_mls** | **str** | The mls of the Inscription | [optional] 
**s_inscription_contract** | **str** | The sale contract number | 
**i_inscription_sellerdeclaration** | **int** | The seller declaration number of the Inscription | 
**e_inscription_type** | [**FieldEInscriptionType**](FieldEInscriptionType.md) |  | 
**d_inscription_initialsaleprice** | **str** | The initial sale price of the Inscription | 
**d_inscription_saleprice** | **str** | The saleprice of the Inscription | 
**d_inscription_rentprice** | **str** | The rent price of the Inscription | 
**e_inscription_remunerationtype** | [**FieldEInscriptionRemunerationtype**](FieldEInscriptionRemunerationtype.md) |  | 
**e_inscription_remunerationinscriptorsellertype** | [**FieldEInscriptionRemunerationinscriptorsellertype**](FieldEInscriptionRemunerationinscriptorsellertype.md) |  | 
**e_inscription_remunerationreferencetype** | [**FieldEInscriptionRemunerationreferencetype**](FieldEInscriptionRemunerationreferencetype.md) |  | 
**e_inscription_remunerationtotaltype** | [**FieldEInscriptionRemunerationtotaltype**](FieldEInscriptionRemunerationtotaltype.md) |  | 
**d_inscription_remuneration** | **str** | The remuneration amount of the Inscription | 
**d_inscription_remunerationinscriptorseller** | **str** | The remuneration amount for the inscriptor or seller of the Inscription | 
**d_inscription_remunerationreference** | **str** | The remuneration amount for the reference of the Inscription | 
**d_inscription_remunerationtotal** | **str** | The remuneration amount total of the Inscription | 
**d_inscription_mortgagesold** | **str** | The balande for the mortgage of the Inscription | 
**dt_inscription_date** | **str** | The date of the Inscription | [optional] 
**dt_inscription_cancellationdate** | **str** | The cancellation date of the Inscription | [optional] 
**dt_inscription_initialexpirationdate** | **str** | The initial expiration date of the Inscription | [optional] 
**dt_inscription_expirationdate** | **str** | The expiration date of the Inscription | [optional] 
**dt_inscription_notarydate** | **str** | The notary date of the Inscription | [optional] 
**dt_inscription_notaryentereddate** | **str** | The notary entered date of the Inscription | [optional] 
**t_inscription_cadastre** | **str** | The cadastre of the Inscription | 
**b_inscription_reference** | **bool** | Whether if it&#39;s an reference | 
**b_inscription_inspection** | **bool** | Whether the inscription can be acces by an inspector | 
**b_inscription_isactive** | **bool** | Whether the inscription is active or not | 
**t_inscription_checklistnote** | **str** | The checklist note of the Inscription | 
**b_inscription_new** | **bool** | Whether if it&#39;s an new | 
**b_inscription_homeowner** | **bool** | Whether if it&#39;s an homeowner | 
**b_inscription_archived** | **bool** | Whether the inscription is archived or not | 
**b_inscription_litigation** | **bool** | Whether if it&#39;s an litigation | 
**b_inscription_repossession** | **bool** | Whether if it&#39;s an repossession | 
**b_inscription_issolicitation** | **bool** | Whether if it&#39;s a solicitation | 
**b_inscription_salebyowner** | **bool** | Whether if it&#39;s a sale by the owner | 
**b_inscription_soldwithoutlegalwarranty** | **bool** | Whether if it&#39;s sold without the legal warranty | 
**i_inscription_constructionyear** | **int** | The construction year of the Inscription | 
**i_inscription_unit** | **int** | The number of unit for the Inscription | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.inscription_response_compound import InscriptionResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionResponseCompound from a JSON string
inscription_response_compound_instance = InscriptionResponseCompound.from_json(json)
# print the JSON string representation of the object
print(InscriptionResponseCompound.to_json())

# convert the object into a dict
inscription_response_compound_dict = inscription_response_compound_instance.to_dict()
# create an instance of InscriptionResponseCompound from a dict
inscription_response_compound_from_dict = InscriptionResponseCompound.from_dict(inscription_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


