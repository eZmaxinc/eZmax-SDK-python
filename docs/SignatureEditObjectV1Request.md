# SignatureEditObjectV1Request

Request for PUT /1/object/signature/{pkiSignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_signature** | [**SignatureRequestCompound**](SignatureRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.signature_edit_object_v1_request import SignatureEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureEditObjectV1Request from a JSON string
signature_edit_object_v1_request_instance = SignatureEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(SignatureEditObjectV1Request.to_json())

# convert the object into a dict
signature_edit_object_v1_request_dict = signature_edit_object_v1_request_instance.to_dict()
# create an instance of SignatureEditObjectV1Request from a dict
signature_edit_object_v1_request_form_dict = signature_edit_object_v1_request.from_dict(signature_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


