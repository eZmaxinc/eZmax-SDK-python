# CreditcardclientRequestPatch

A Creditcardclient Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_creditcardclientrelation_isdefault** | **bool** | Whether if it&#39;s the creditcardclient is the default one | [optional] 

## Example

```python
from eZmaxApi.models.creditcardclient_request_patch import CreditcardclientRequestPatch

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardclientRequestPatch from a JSON string
creditcardclient_request_patch_instance = CreditcardclientRequestPatch.from_json(json)
# print the JSON string representation of the object
print(CreditcardclientRequestPatch.to_json())

# convert the object into a dict
creditcardclient_request_patch_dict = creditcardclient_request_patch_instance.to_dict()
# create an instance of CreditcardclientRequestPatch from a dict
creditcardclient_request_patch_from_dict = CreditcardclientRequestPatch.from_dict(creditcardclient_request_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


