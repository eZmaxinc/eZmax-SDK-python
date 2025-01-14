# PaymenttermCreateObjectV1Request

Request for POST /1/object/paymentterm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_paymentterm** | [**List[PaymenttermRequestCompound]**](PaymenttermRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.paymentterm_create_object_v1_request import PaymenttermCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of PaymenttermCreateObjectV1Request from a JSON string
paymentterm_create_object_v1_request_instance = PaymenttermCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(PaymenttermCreateObjectV1Request.to_json())

# convert the object into a dict
paymentterm_create_object_v1_request_dict = paymentterm_create_object_v1_request_instance.to_dict()
# create an instance of PaymenttermCreateObjectV1Request from a dict
paymentterm_create_object_v1_request_from_dict = PaymenttermCreateObjectV1Request.from_dict(paymentterm_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


