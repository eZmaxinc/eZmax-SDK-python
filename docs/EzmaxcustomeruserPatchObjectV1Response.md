# EzmaxcustomeruserPatchObjectV1Response

Request for PATCH /1/object/ezmaxcustomeruser/{pkiEzmaxcustomeruserID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezmaxcustomeruser_patch_object_v1_response import EzmaxcustomeruserPatchObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxcustomeruserPatchObjectV1Response from a JSON string
ezmaxcustomeruser_patch_object_v1_response_instance = EzmaxcustomeruserPatchObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzmaxcustomeruserPatchObjectV1Response.to_json())

# convert the object into a dict
ezmaxcustomeruser_patch_object_v1_response_dict = ezmaxcustomeruser_patch_object_v1_response_instance.to_dict()
# create an instance of EzmaxcustomeruserPatchObjectV1Response from a dict
ezmaxcustomeruser_patch_object_v1_response_from_dict = EzmaxcustomeruserPatchObjectV1Response.from_dict(ezmaxcustomeruser_patch_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


