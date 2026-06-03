# InscriptionnotauthenticatedListElement

A Inscriptionnotauthenticated List Element

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
**b_inscription_inspection** | **bool** | Whether the inscription can be acces by an inspector | [optional] 
**b_inscription_isactive** | **bool** | Whether the inscription is active or not | 
**b_inscription_archived** | **bool** | Whether the inscription is archived or not | 
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
**fki_province_id** | **int** | The unique ID of the Province.  Here are some common values (Complete list must be retrieved from API):  |Value|Description| |-|-| |1|(Canada) Alberta |2|(Canada) British Columbia| |3|(Canada) Manitoba| |3|(Canada) Manitoba| |4|(Canada) New Brunswick| |5|(Canada) Newfoundland| |6|(Canada) Northwest Territories| |7|(Canada) Nova Scotia| |8|(Canada) Nunavut| |9|(Canada) Ontario| |10|(Canada) Prince Edward Island| |11|(Canada) Quebec| |12|(Canada) Saskatchewan| |13|(Canada) Yukon| |14|(United-States) Alabama| |15|(United-States) Alaska| |16|(United-States) Arizona| |17|(United-States) Arkansas| |18|(United-States) California| |19|(United-States) Colorado| |20|(United-States) Connecticut| |21|(United-States) Delaware| |22|(United-States) District of Columbia| |23|(United-States) Florida| |24|(United-States) Georgia| |25|(United-States) Hawaii| |26|(United-States) Idaho| |27|(United-States) Illinois| |28|(United-States) Indiana| |29|(United-States) Iowa| |30|(United-States) Kansas| |31|(United-States) Kentucky| |32|(United-States) Louisiane| |33|(United-States) Maine| |34|(United-States) Maryland| |35|(United-States) Massachusetts| |36|(United-States) Michigan| |37|(United-States) Minnesota| |38|(United-States) Mississippi| |39|(United-States) Missouri| |40|(United-States) Montana| |41|(United-States) Nebraska| |42|(United-States) Nevada| |43|(United-States) New Hampshire| |44|(United-States) New Jersey| |45|(United-States) New Mexico| |46|(United-States) New York| |47|(United-States) North Carolina| |48|(United-States) North Dakota| |49|(United-States) Ohio| |50|(United-States) Oklahoma| |51|(United-States) Oregon| |52|(United-States) Pennsylvania| |53|(United-States) Rhode Island| |54|(United-States) South Carolina| |55|(United-States) South Dakota| |56|(United-States) Tennessee| |57|(United-States) Texas| |58|(United-States) Utah| |60|(United-States) Vermont| |59|(United-States) Virginia| |61|(United-States) Washington| |62|(United-States) West Virginia| |63|(United-States) Wisconsin| |64|(United-States) Wyoming| | [optional] 
**s_province_name_x** | **str** | The name of the Province in the language of the requester | [optional] 
**fki_country_id** | **int** | The unique ID of the Country.  Here are some common values (Complete list must be retrieved from API):  |Value|Description| |-|-| |1|Canada| |2|United-States| | [optional] 
**s_country_name_x** | **str** | The name of the Country in the language of the requester | [optional] 
**s_inscriptionnotauthenticated_offertopurchasenumber** | **str** | The Offer to purchase number | 

## Example

```python
from eZmaxApi.models.inscriptionnotauthenticated_list_element import InscriptionnotauthenticatedListElement

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionnotauthenticatedListElement from a JSON string
inscriptionnotauthenticated_list_element_instance = InscriptionnotauthenticatedListElement.from_json(json)
# print the JSON string representation of the object
print(InscriptionnotauthenticatedListElement.to_json())

# convert the object into a dict
inscriptionnotauthenticated_list_element_dict = inscriptionnotauthenticated_list_element_instance.to_dict()
# create an instance of InscriptionnotauthenticatedListElement from a dict
inscriptionnotauthenticated_list_element_from_dict = InscriptionnotauthenticatedListElement.from_dict(inscriptionnotauthenticated_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


