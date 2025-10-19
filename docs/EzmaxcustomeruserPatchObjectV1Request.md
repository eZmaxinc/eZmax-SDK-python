# EzmaxcustomeruserPatchObjectV1Request

Request for PATCH /1/object/ezmaxcustomeruser/{pkiEzmaxcustomeruserID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezmaxcustomeruser** | [**EzmaxcustomeruserRequestPatch**](EzmaxcustomeruserRequestPatch.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxcustomeruser_patch_object_v1_request import EzmaxcustomeruserPatchObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxcustomeruserPatchObjectV1Request from a JSON string
ezmaxcustomeruser_patch_object_v1_request_instance = EzmaxcustomeruserPatchObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzmaxcustomeruserPatchObjectV1Request.to_json())

# convert the object into a dict
ezmaxcustomeruser_patch_object_v1_request_dict = ezmaxcustomeruser_patch_object_v1_request_instance.to_dict()
# create an instance of EzmaxcustomeruserPatchObjectV1Request from a dict
ezmaxcustomeruser_patch_object_v1_request_from_dict = EzmaxcustomeruserPatchObjectV1Request.from_dict(ezmaxcustomeruser_patch_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


