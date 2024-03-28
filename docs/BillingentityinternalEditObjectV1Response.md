# BillingentityinternalEditObjectV1Response

Response for PUT /1/object/billingentityinternal/{pkiBillingentityinternalID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.billingentityinternal_edit_object_v1_response import BillingentityinternalEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalEditObjectV1Response from a JSON string
billingentityinternal_edit_object_v1_response_instance = BillingentityinternalEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(BillingentityinternalEditObjectV1Response.to_json())

# convert the object into a dict
billingentityinternal_edit_object_v1_response_dict = billingentityinternal_edit_object_v1_response_instance.to_dict()
# create an instance of BillingentityinternalEditObjectV1Response from a dict
billingentityinternal_edit_object_v1_response_form_dict = billingentityinternal_edit_object_v1_response.from_dict(billingentityinternal_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


