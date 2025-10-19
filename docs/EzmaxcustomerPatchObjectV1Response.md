# EzmaxcustomerPatchObjectV1Response

Request for PATCH /1/object/ezmaxcustomer/{pkiEzmaxcustomerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezmaxcustomer_patch_object_v1_response import EzmaxcustomerPatchObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxcustomerPatchObjectV1Response from a JSON string
ezmaxcustomer_patch_object_v1_response_instance = EzmaxcustomerPatchObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzmaxcustomerPatchObjectV1Response.to_json())

# convert the object into a dict
ezmaxcustomer_patch_object_v1_response_dict = ezmaxcustomer_patch_object_v1_response_instance.to_dict()
# create an instance of EzmaxcustomerPatchObjectV1Response from a dict
ezmaxcustomer_patch_object_v1_response_from_dict = EzmaxcustomerPatchObjectV1Response.from_dict(ezmaxcustomer_patch_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


