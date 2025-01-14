# BrandingCreateObjectV2Request

Request for POST /2/object/branding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_branding** | [**List[BrandingRequestCompoundV2]**](BrandingRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.branding_create_object_v2_request import BrandingCreateObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingCreateObjectV2Request from a JSON string
branding_create_object_v2_request_instance = BrandingCreateObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(BrandingCreateObjectV2Request.to_json())

# convert the object into a dict
branding_create_object_v2_request_dict = branding_create_object_v2_request_instance.to_dict()
# create an instance of BrandingCreateObjectV2Request from a dict
branding_create_object_v2_request_from_dict = BrandingCreateObjectV2Request.from_dict(branding_create_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


