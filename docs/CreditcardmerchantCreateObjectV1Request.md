# CreditcardmerchantCreateObjectV1Request

Request for POST /1/object/creditcardmerchant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_creditcardmerchant** | [**List[CreditcardmerchantRequestCompound]**](CreditcardmerchantRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardmerchant_create_object_v1_request import CreditcardmerchantCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardmerchantCreateObjectV1Request from a JSON string
creditcardmerchant_create_object_v1_request_instance = CreditcardmerchantCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(CreditcardmerchantCreateObjectV1Request.to_json())

# convert the object into a dict
creditcardmerchant_create_object_v1_request_dict = creditcardmerchant_create_object_v1_request_instance.to_dict()
# create an instance of CreditcardmerchantCreateObjectV1Request from a dict
creditcardmerchant_create_object_v1_request_from_dict = CreditcardmerchantCreateObjectV1Request.from_dict(creditcardmerchant_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


