# CreditcarddetailRequest

A Creditcarddetail Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_creditcarddetail_expirationmonth** | **int** | The expirationmonth of the Creditcarddetail | 
**i_creditcarddetail_expirationyear** | **int** | The expirationyear of the Creditcarddetail | 
**s_creditcarddetail_civic** | **str** | The civic of the Creditcarddetail | 
**s_creditcarddetail_street** | **str** | The street of the Creditcarddetail | 
**s_creditcarddetail_zip** | **str** | The zip of the Creditcarddetail | 

## Example

```python
from eZmaxApi.models.creditcarddetail_request import CreditcarddetailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcarddetailRequest from a JSON string
creditcarddetail_request_instance = CreditcarddetailRequest.from_json(json)
# print the JSON string representation of the object
print(CreditcarddetailRequest.to_json())

# convert the object into a dict
creditcarddetail_request_dict = creditcarddetail_request_instance.to_dict()
# create an instance of CreditcarddetailRequest from a dict
creditcarddetail_request_from_dict = CreditcarddetailRequest.from_dict(creditcarddetail_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


