# SignatureRequestCompound

A Signature Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_signature_id** | **int** | The unique ID of the Signature | [optional] 
**fki_font_id** | **int** | The unique ID of the Font | 
**e_signature_preference** | [**FieldESignaturePreference**](FieldESignaturePreference.md) |  | 
**t_signature_svg** | **str** | The svg of the Signature | [optional] 
**t_signature_svginitials** | **str** | The svg of the Initials | [optional] 

## Example

```python
from eZmaxApi.models.signature_request_compound import SignatureRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureRequestCompound from a JSON string
signature_request_compound_instance = SignatureRequestCompound.from_json(json)
# print the JSON string representation of the object
print(SignatureRequestCompound.to_json())

# convert the object into a dict
signature_request_compound_dict = signature_request_compound_instance.to_dict()
# create an instance of SignatureRequestCompound from a dict
signature_request_compound_from_dict = SignatureRequestCompound.from_dict(signature_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


