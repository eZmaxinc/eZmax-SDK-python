# PaymenttermEditObjectV1Request

Request for PUT /1/object/paymentterm/{pkiPaymenttermID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_paymentterm** | [**PaymenttermRequestCompound**](PaymenttermRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.paymentterm_edit_object_v1_request import PaymenttermEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of PaymenttermEditObjectV1Request from a JSON string
paymentterm_edit_object_v1_request_instance = PaymenttermEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print PaymenttermEditObjectV1Request.to_json()

# convert the object into a dict
paymentterm_edit_object_v1_request_dict = paymentterm_edit_object_v1_request_instance.to_dict()
# create an instance of PaymenttermEditObjectV1Request from a dict
paymentterm_edit_object_v1_request_form_dict = paymentterm_edit_object_v1_request.from_dict(paymentterm_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


