# CreditcardmerchantEditObjectV1Request

Request for PUT /1/object/creditcardmerchant/{pkiCreditcardmerchantID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_creditcardmerchant** | [**CreditcardmerchantRequestCompound**](CreditcardmerchantRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardmerchant_edit_object_v1_request import CreditcardmerchantEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardmerchantEditObjectV1Request from a JSON string
creditcardmerchant_edit_object_v1_request_instance = CreditcardmerchantEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(CreditcardmerchantEditObjectV1Request.to_json())

# convert the object into a dict
creditcardmerchant_edit_object_v1_request_dict = creditcardmerchant_edit_object_v1_request_instance.to_dict()
# create an instance of CreditcardmerchantEditObjectV1Request from a dict
creditcardmerchant_edit_object_v1_request_from_dict = CreditcardmerchantEditObjectV1Request.from_dict(creditcardmerchant_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


