# BrandingCreateObjectV1Request

Request for POST /1/object/branding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_branding** | [**List[BrandingRequestCompound]**](BrandingRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.branding_create_object_v1_request import BrandingCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingCreateObjectV1Request from a JSON string
branding_create_object_v1_request_instance = BrandingCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print BrandingCreateObjectV1Request.to_json()

# convert the object into a dict
branding_create_object_v1_request_dict = branding_create_object_v1_request_instance.to_dict()
# create an instance of BrandingCreateObjectV1Request from a dict
branding_create_object_v1_request_form_dict = branding_create_object_v1_request.from_dict(branding_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


