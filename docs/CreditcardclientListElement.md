# CreditcardclientListElement

A Creditcardclient List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_creditcardclient_id** | **int** | The unique ID of the Creditcardclient | 
**fki_creditcarddetail_id** | **int** | The unique ID of the Creditcarddetail | 
**b_creditcardclientrelation_isdefault** | **bool** | Whether if it&#39;s an relationisdefault | 
**s_creditcardclient_description** | **str** | The description of the Creditcardclient | 
**b_creditcardclient_isactive** | **bool** | Whether the creditcardclient is active or not | 
**b_creditcardclient_allowedagencypayment** | **bool** | Whether if it&#39;s an allowedagencypayment | 
**b_creditcardclient_allowedroyallepageprotection** | **bool** | Whether if it&#39;s an allowedroyallepageprotection | 
**b_creditcardclient_allowedtranquillit** | **bool** | Whether if it&#39;s an allowedtranquillit | 
**i_creditcarddetail_expirationmonth** | **int** | The expirationmonth of the Creditcarddetail | 
**i_creditcarddetail_expirationyear** | **int** | The expirationyear of the Creditcarddetail | 
**s_creditcarddetail_numbermasked** | **str** | The numbermasked of the Creditcarddetail | 

## Example

```python
from eZmaxApi.models.creditcardclient_list_element import CreditcardclientListElement

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardclientListElement from a JSON string
creditcardclient_list_element_instance = CreditcardclientListElement.from_json(json)
# print the JSON string representation of the object
print(CreditcardclientListElement.to_json())

# convert the object into a dict
creditcardclient_list_element_dict = creditcardclient_list_element_instance.to_dict()
# create an instance of CreditcardclientListElement from a dict
creditcardclient_list_element_form_dict = creditcardclient_list_element.from_dict(creditcardclient_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


