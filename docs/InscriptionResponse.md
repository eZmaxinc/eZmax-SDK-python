# InscriptionResponse

A Inscription Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_inscription_id** | **int** | The unique ID of the Inscription. | 
**fki_company_id** | **int** | The unique ID of the Company | 
**s_company_name_x** | **str** | The Name of the Company in the language of the requester | [optional] 
**fki_department_id** | **int** | The unique ID of the Department | 
**s_department_name_x** | **str** | The Name of the Department in the language of the requester | [optional] 
**fki_realestateboard_id** | **int** | The unique ID of the Realestateboard | 
**s_realestateboard_name_x** | **str** | The name of the Realestateboard | [optional] 
**fki_address_id** | **int** | The unique ID of the Address | 
**s_address** | **str** | The complete address in a single line | [optional] 
**fki_inscriptionbuildingtype_id** | **int** | The unique ID of the Inscriptionbuildingtype | 
**s_inscriptionbuildingtype_name_x** | **str** | The name of the Inscriptionbuildingtype in the language of the requester | [optional] 
**fki_inscriptiontype_id** | **int** | The unique ID of the Inscriptiontype | 
**s_inscriptiontype_name_x** | **str** | The name of the Inscriptiontype in the language of the requester | [optional] 
**fki_inscriptioncategory_id** | **int** | The unique ID of the Inscriptioncategory | 
**s_inscriptioncategory_name_x** | **str** | The name of the Inscriptioncategory in the language of the requester | [optional] 
**e_inscription_step** | [**FieldEInscriptionStep**](FieldEInscriptionStep.md) |  | 
**e_inscription_residence_type** | [**FieldEInscriptionResidenceType**](FieldEInscriptionResidenceType.md) |  | 
**s_inscription_civicend** | **str** | The civicend of the Inscription | 
**s_inscription_mls** | **str** | The mls of the Inscription | 
**s_inscription_contract** | **str** | The sale contract number | 
**i_inscription_sellerdeclaration** | **int** | The sellerdeclaration of the Inscription | 
**e_inscription_type** | [**FieldEInscriptionType**](FieldEInscriptionType.md) |  | 
**d_inscription_initialsaleprice** | **str** | The initialsaleprice of the Inscription | 
**d_inscription_saleprice** | **str** | The saleprice of the Inscription | 
**d_inscription_rentprice** | **str** | The rentprice of the Inscription | 
**e_inscription_remunerationtype** | [**FieldEInscriptionRemunerationtype**](FieldEInscriptionRemunerationtype.md) |  | 
**e_inscription_remunerationinscriptorsellertype** | [**FieldEInscriptionRemunerationinscriptorsellertype**](FieldEInscriptionRemunerationinscriptorsellertype.md) |  | 
**e_inscription_remunerationreferencetype** | [**FieldEInscriptionRemunerationreferencetype**](FieldEInscriptionRemunerationreferencetype.md) |  | 
**e_inscription_remunerationtotaltype** | [**FieldEInscriptionRemunerationtotaltype**](FieldEInscriptionRemunerationtotaltype.md) |  | 
**d_inscription_remuneration** | **str** | The remuneration of the Inscription | 
**d_inscription_remunerationinscriptorseller** | **str** | The remunerationinscriptorseller of the Inscription | 
**d_inscription_remunerationreference** | **str** | The remunerationreference of the Inscription | 
**d_inscription_remunerationtotal** | **str** | The remunerationtotal of the Inscription | 
**d_inscription_mortgagesold** | **str** | The mortgagesold of the Inscription | 
**dt_inscription_date** | **str** | The date of the Inscription | 
**dt_inscription_cancellationdate** | **str** | The cancellationdate of the Inscription | 
**dt_inscription_initialexpirationdate** | **str** | The initialexpirationdate of the Inscription | 
**dt_inscription_expirationdate** | **str** | The expirationdate of the Inscription | 
**dt_inscription_notarydate** | **str** | The notarydate of the Inscription | 
**dt_inscription_notaryentereddate** | **str** | The notaryentereddate of the Inscription | 
**t_inscription_cadastre** | **str** | The cadastre of the Inscription | 
**b_inscription_reference** | **bool** | Whether if it&#39;s an reference | 
**b_inscription_inspection** | **bool** | Whether the inscription can be acces by an inspector | 
**b_inscription_isactive** | **bool** | Whether the inscription is active or not | 
**t_inscription_checklistnote** | **str** | The checklistnote of the Inscription | 
**b_inscription_new** | **bool** | Whether if it&#39;s an new | 
**b_inscription_homeowner** | **bool** | Whether if it&#39;s an homeowner | 
**b_inscription_archived** | **bool** | Whether the inscription is archived or not | 
**b_inscription_litigation** | **bool** | Whether if it&#39;s an litigation | 
**b_inscription_repossession** | **bool** | Whether if it&#39;s an repossession | 
**b_inscription_issolicitation** | **bool** | Whether if it&#39;s an issolicitation | 
**b_inscription_salebyowner** | **bool** | Whether if it&#39;s an salebyowner | 
**b_inscription_soldwithoutlegalwarranty** | **bool** | Whether if it&#39;s an soldwithoutlegalwarranty | 
**i_inscription_constructionyear** | **int** | The constructionyear of the Inscription | 
**i_inscription_unit** | **int** | The unit of the Inscription | 

## Example

```python
from eZmaxApi.models.inscription_response import InscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionResponse from a JSON string
inscription_response_instance = InscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(InscriptionResponse.to_json())

# convert the object into a dict
inscription_response_dict = inscription_response_instance.to_dict()
# create an instance of InscriptionResponse from a dict
inscription_response_from_dict = InscriptionResponse.from_dict(inscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


