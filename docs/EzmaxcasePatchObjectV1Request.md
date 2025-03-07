# EzmaxcasePatchObjectV1Request

Request for PATCH /1/object/ezmaxcase/{pkiEzmaxcaseID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezmaxcase** | [**EzmaxcaseRequestPatch**](EzmaxcaseRequestPatch.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxcase_patch_object_v1_request import EzmaxcasePatchObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxcasePatchObjectV1Request from a JSON string
ezmaxcase_patch_object_v1_request_instance = EzmaxcasePatchObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzmaxcasePatchObjectV1Request.to_json())

# convert the object into a dict
ezmaxcase_patch_object_v1_request_dict = ezmaxcase_patch_object_v1_request_instance.to_dict()
# create an instance of EzmaxcasePatchObjectV1Request from a dict
ezmaxcase_patch_object_v1_request_from_dict = EzmaxcasePatchObjectV1Request.from_dict(ezmaxcase_patch_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


