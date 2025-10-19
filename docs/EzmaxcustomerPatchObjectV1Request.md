# EzmaxcustomerPatchObjectV1Request

Request for PATCH /1/object/ezmaxcustomer/{pkiEzmaxcustomerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezmaxcustomer** | [**EzmaxcustomerRequestPatch**](EzmaxcustomerRequestPatch.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxcustomer_patch_object_v1_request import EzmaxcustomerPatchObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxcustomerPatchObjectV1Request from a JSON string
ezmaxcustomer_patch_object_v1_request_instance = EzmaxcustomerPatchObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzmaxcustomerPatchObjectV1Request.to_json())

# convert the object into a dict
ezmaxcustomer_patch_object_v1_request_dict = ezmaxcustomer_patch_object_v1_request_instance.to_dict()
# create an instance of EzmaxcustomerPatchObjectV1Request from a dict
ezmaxcustomer_patch_object_v1_request_from_dict = EzmaxcustomerPatchObjectV1Request.from_dict(ezmaxcustomer_patch_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


