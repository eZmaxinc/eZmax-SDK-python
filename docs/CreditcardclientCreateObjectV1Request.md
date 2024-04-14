# CreditcardclientCreateObjectV1Request

Request for POST /1/object/creditcardclient

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_creditcardclient** | [**List[CreditcardclientRequestCompound]**](CreditcardclientRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardclient_create_object_v1_request import CreditcardclientCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardclientCreateObjectV1Request from a JSON string
creditcardclient_create_object_v1_request_instance = CreditcardclientCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(CreditcardclientCreateObjectV1Request.to_json())

# convert the object into a dict
creditcardclient_create_object_v1_request_dict = creditcardclient_create_object_v1_request_instance.to_dict()
# create an instance of CreditcardclientCreateObjectV1Request from a dict
creditcardclient_create_object_v1_request_form_dict = creditcardclient_create_object_v1_request.from_dict(creditcardclient_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


