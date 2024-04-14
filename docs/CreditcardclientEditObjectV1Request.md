# CreditcardclientEditObjectV1Request

Request for PUT /1/object/creditcardclient/{pkiCreditcardclientID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_creditcardclient** | [**CreditcardclientRequestCompound**](CreditcardclientRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardclient_edit_object_v1_request import CreditcardclientEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardclientEditObjectV1Request from a JSON string
creditcardclient_edit_object_v1_request_instance = CreditcardclientEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(CreditcardclientEditObjectV1Request.to_json())

# convert the object into a dict
creditcardclient_edit_object_v1_request_dict = creditcardclient_edit_object_v1_request_instance.to_dict()
# create an instance of CreditcardclientEditObjectV1Request from a dict
creditcardclient_edit_object_v1_request_form_dict = creditcardclient_edit_object_v1_request.from_dict(creditcardclient_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


