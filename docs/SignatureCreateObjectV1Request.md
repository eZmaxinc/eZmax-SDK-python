# SignatureCreateObjectV1Request

Request for POST /1/object/signature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_signature** | [**List[SignatureRequestCompound]**](SignatureRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.signature_create_object_v1_request import SignatureCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureCreateObjectV1Request from a JSON string
signature_create_object_v1_request_instance = SignatureCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print SignatureCreateObjectV1Request.to_json()

# convert the object into a dict
signature_create_object_v1_request_dict = signature_create_object_v1_request_instance.to_dict()
# create an instance of SignatureCreateObjectV1Request from a dict
signature_create_object_v1_request_form_dict = signature_create_object_v1_request.from_dict(signature_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


