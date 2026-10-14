# AdjustmentreminderGetListV1Response

Response for GET /1/object/adjustmentreminder/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AdjustmentreminderGetListV1ResponseMPayload**](AdjustmentreminderGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.adjustmentreminder_get_list_v1_response import AdjustmentreminderGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentreminderGetListV1Response from a JSON string
adjustmentreminder_get_list_v1_response_instance = AdjustmentreminderGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(AdjustmentreminderGetListV1Response.to_json())

# convert the object into a dict
adjustmentreminder_get_list_v1_response_dict = adjustmentreminder_get_list_v1_response_instance.to_dict()
# create an instance of AdjustmentreminderGetListV1Response from a dict
adjustmentreminder_get_list_v1_response_from_dict = AdjustmentreminderGetListV1Response.from_dict(adjustmentreminder_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


