# EzmaxcasePatchObjectV1Response

Response for PATCH /1/object/creditcardclient/{pkiCreditcardclientID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezmaxcase_patch_object_v1_response import EzmaxcasePatchObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxcasePatchObjectV1Response from a JSON string
ezmaxcase_patch_object_v1_response_instance = EzmaxcasePatchObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzmaxcasePatchObjectV1Response.to_json())

# convert the object into a dict
ezmaxcase_patch_object_v1_response_dict = ezmaxcase_patch_object_v1_response_instance.to_dict()
# create an instance of EzmaxcasePatchObjectV1Response from a dict
ezmaxcase_patch_object_v1_response_from_dict = EzmaxcasePatchObjectV1Response.from_dict(ezmaxcase_patch_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


