# PaymenttermEditObjectV1Response

Response for PUT /1/object/paymentterm/{pkiPaymenttermID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.paymentterm_edit_object_v1_response import PaymenttermEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymenttermEditObjectV1Response from a JSON string
paymentterm_edit_object_v1_response_instance = PaymenttermEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(PaymenttermEditObjectV1Response.to_json())

# convert the object into a dict
paymentterm_edit_object_v1_response_dict = paymentterm_edit_object_v1_response_instance.to_dict()
# create an instance of PaymenttermEditObjectV1Response from a dict
paymentterm_edit_object_v1_response_form_dict = paymentterm_edit_object_v1_response.from_dict(paymentterm_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


