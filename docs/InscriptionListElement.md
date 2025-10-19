# InscriptionListElement

A Inscription List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_inscription_id** | **int** | The unique ID of the Inscription. | 
**pki_inscriptionnotauthenticated_id** | **int** | The unique ID of the Inscriptionnotauthenticated. | [optional] 
**fki_inscriptiontype_id** | **int** | The unique ID of the Inscriptiontype | 
**s_inscriptiontype_name_x** | **str** | The name of the Inscriptiontype in the language of the requester | 
**e_inscription_step** | [**FieldEInscriptionStep**](FieldEInscriptionStep.md) |  | 
**s_inscription_civicend** | **str** | The civicend of the Inscription | 
**s_inscription_mls** | **str** | The mls of the Inscription | [optional] 
**d_inscription_saleprice** | **str** | The saleprice of the Inscription | 
**d_inscription_rentprice** | **str** | The rentprice of the Inscription | 
**dt_inscription_date** | **str** | The date of the Inscription | [optional] 
**dt_inscription_expirationdate** | **str** | The expirationdate of the Inscription | [optional] 
**dt_inscription_notarydate** | **str** | The notarydate of the Inscription | [optional] 
**b_inscription_isactive** | **bool** | Whether the inscription is active or not | 
**b_inscription_archived** | **bool** | Whether the inscription is archived or not | 
**b_inscription_inspection** | **bool** | Whether the inscription can be acces by an inspector | [optional] 
**dt_inscriptionnotauthenticated_notaryscheduledate** | **str** | The notaryscheduledate of the Inscriptionnotauthenticated | [optional] 
**dt_inscriptionnotauthenticated_transactiondate** | **str** | The transactiondate of the Inscriptionnotauthenticated | [optional] 
**dt_inscriptionnotauthenticated_transactiondate_real** | **str** | The transactiondatereal of the Inscriptionnotauthenticated | [optional] 
**b_inscriptionnotauthenticated_conditional** | **bool** | Whether the inscriptionnotauthenticated is conditional | [optional] 
**b_inscriptionnotauthenticated_isactive** | **bool** | Whether the inscriptionnotauthenticated is active or not | [optional] 
**s_address_civic** | **str** | The Civic number. | [optional] 
**s_address_street** | **str** | The Street Name | [optional] 
**s_address_suite** | **str** | The Suite or appartment number | [optional] 
**s_address_city** | **str** | The City name | [optional] 
**s_address_zip** | **str** | The Postal/Zip Code  The value must be entered without spaces | [optional] 
**s_province_name_x** | **str** | The name of the Province in the language of the requester | [optional] 
**s_country_name_x** | **str** | The name of the Country in the language of the requester | [optional] 
**i_inscriptionnotauthenticated_canceled** | **int** | The numbre of inscriptionnotauthenticated was canceled in this Inscription | 
**b_allowed_copyintoinscriptionedm** | **bool** | Whether we are allowed to copy into the Inscription EDM | 

## Example

```python
from eZmaxApi.models.inscription_list_element import InscriptionListElement

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionListElement from a JSON string
inscription_list_element_instance = InscriptionListElement.from_json(json)
# print the JSON string representation of the object
print(InscriptionListElement.to_json())

# convert the object into a dict
inscription_list_element_dict = inscription_list_element_instance.to_dict()
# create an instance of InscriptionListElement from a dict
inscription_list_element_from_dict = InscriptionListElement.from_dict(inscription_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


