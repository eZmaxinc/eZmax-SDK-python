# CreditcarddetailResponse

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
from eZmaxApi.models.creditcarddetail_response import CreditcarddetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcarddetailResponse from a JSON string
creditcarddetail_response_instance = CreditcarddetailResponse.from_json(json)
# print the JSON string representation of the object
print(CreditcarddetailResponse.to_json())

# convert the object into a dict
creditcarddetail_response_dict = creditcarddetail_response_instance.to_dict()
# create an instance of CreditcarddetailResponse from a dict
creditcarddetail_response_form_dict = creditcarddetail_response.from_dict(creditcarddetail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


