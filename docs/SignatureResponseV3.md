# SignatureResponseV3

A Signature Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_signature_id** | **int** | The unique ID of the Signature | 
**fki_font_id** | **int** | The unique ID of the Font | 
**e_signature_preference** | [**FieldESignaturePreference**](FieldESignaturePreference.md) |  | 
**b_signature_svg** | **bool** | Whether the signature has a SVG or not | 
**b_signature_svginitials** | **bool** | Whether the initials has a SVG or not | 

## Example

```python
from eZmaxApi.models.signature_response_v3 import SignatureResponseV3

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureResponseV3 from a JSON string
signature_response_v3_instance = SignatureResponseV3.from_json(json)
# print the JSON string representation of the object
print(SignatureResponseV3.to_json())

# convert the object into a dict
signature_response_v3_dict = signature_response_v3_instance.to_dict()
# create an instance of SignatureResponseV3 from a dict
signature_response_v3_from_dict = SignatureResponseV3.from_dict(signature_response_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


