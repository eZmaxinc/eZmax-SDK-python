# CreditcardclientPatchObjectV1Response

Response for PATCH /1/object/creditcardclient/{pkiCreditcardclientID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from eZmaxApi.models.creditcardclient_patch_object_v1_response import CreditcardclientPatchObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardclientPatchObjectV1Response from a JSON string
creditcardclient_patch_object_v1_response_instance = CreditcardclientPatchObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(CreditcardclientPatchObjectV1Response.to_json())

# convert the object into a dict
creditcardclient_patch_object_v1_response_dict = creditcardclient_patch_object_v1_response_instance.to_dict()
# create an instance of CreditcardclientPatchObjectV1Response from a dict
creditcardclient_patch_object_v1_response_from_dict = CreditcardclientPatchObjectV1Response.from_dict(creditcardclient_patch_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


