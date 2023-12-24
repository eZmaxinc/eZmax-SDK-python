# BrandingEditObjectV1Request

Request for PUT /1/object/branding/{pkiBrandingID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_branding** | [**BrandingRequestCompound**](BrandingRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.branding_edit_object_v1_request import BrandingEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingEditObjectV1Request from a JSON string
branding_edit_object_v1_request_instance = BrandingEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print BrandingEditObjectV1Request.to_json()

# convert the object into a dict
branding_edit_object_v1_request_dict = branding_edit_object_v1_request_instance.to_dict()
# create an instance of BrandingEditObjectV1Request from a dict
branding_edit_object_v1_request_form_dict = branding_edit_object_v1_request.from_dict(branding_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


