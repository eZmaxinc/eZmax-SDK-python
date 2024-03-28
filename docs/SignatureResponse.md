# SignatureResponse

A Signature Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_signature_id** | **int** | The unique ID of the Signature | 
**s_signature_url** | **str** | The URL of the SVG file for the Signature | 

## Example

```python
from eZmaxApi.models.signature_response import SignatureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureResponse from a JSON string
signature_response_instance = SignatureResponse.from_json(json)
# print the JSON string representation of the object
print(SignatureResponse.to_json())

# convert the object into a dict
signature_response_dict = signature_response_instance.to_dict()
# create an instance of SignatureResponse from a dict
signature_response_form_dict = signature_response.from_dict(signature_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


