# CreditcardclientPatchObjectV1Request

Request for PATCH /1/object/creditcardclient/{pkiCreditcardclientID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_creditcardclient** | [**CreditcardclientRequestPatch**](CreditcardclientRequestPatch.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardclient_patch_object_v1_request import CreditcardclientPatchObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardclientPatchObjectV1Request from a JSON string
creditcardclient_patch_object_v1_request_instance = CreditcardclientPatchObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(CreditcardclientPatchObjectV1Request.to_json())

# convert the object into a dict
creditcardclient_patch_object_v1_request_dict = creditcardclient_patch_object_v1_request_instance.to_dict()
# create an instance of CreditcardclientPatchObjectV1Request from a dict
creditcardclient_patch_object_v1_request_from_dict = CreditcardclientPatchObjectV1Request.from_dict(creditcardclient_patch_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


