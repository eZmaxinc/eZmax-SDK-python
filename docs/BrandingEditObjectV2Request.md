# BrandingEditObjectV2Request

Request for PUT /2/object/branding/{pkiBrandingID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_branding** | [**BrandingRequestCompoundV2**](BrandingRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.branding_edit_object_v2_request import BrandingEditObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingEditObjectV2Request from a JSON string
branding_edit_object_v2_request_instance = BrandingEditObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(BrandingEditObjectV2Request.to_json())

# convert the object into a dict
branding_edit_object_v2_request_dict = branding_edit_object_v2_request_instance.to_dict()
# create an instance of BrandingEditObjectV2Request from a dict
branding_edit_object_v2_request_from_dict = BrandingEditObjectV2Request.from_dict(branding_edit_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


