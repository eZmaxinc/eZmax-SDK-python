# CreditcarddetailResponseCompound

A Creditcarddetail Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_creditcarddetail_id** | **int** | The unique ID of the Creditcarddetail | 
**fki_creditcardtype_id** | **int** | The unique ID of the Creditcardtype | 
**s_creditcarddetail_numbermasked** | **str** | The numbermasked of the Creditcarddetail | 
**i_creditcarddetail_expirationmonth** | **int** | The expirationmonth of the Creditcarddetail | 
**i_creditcarddetail_expirationyear** | **int** | The expirationyear of the Creditcarddetail | 
**s_creditcarddetail_civic** | **str** | The civic of the Creditcarddetail | 
**s_creditcarddetail_street** | **str** | The street of the Creditcarddetail | 
**s_creditcarddetail_zip** | **str** | The zip of the Creditcarddetail | 

## Example

```python
from eZmaxApi.models.creditcarddetail_response_compound import CreditcarddetailResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcarddetailResponseCompound from a JSON string
creditcarddetail_response_compound_instance = CreditcarddetailResponseCompound.from_json(json)
# print the JSON string representation of the object
print(CreditcarddetailResponseCompound.to_json())

# convert the object into a dict
creditcarddetail_response_compound_dict = creditcarddetail_response_compound_instance.to_dict()
# create an instance of CreditcarddetailResponseCompound from a dict
creditcarddetail_response_compound_form_dict = creditcarddetail_response_compound.from_dict(creditcarddetail_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


