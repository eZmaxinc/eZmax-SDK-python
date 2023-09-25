# VersionhistoryGetObjectV2Response

Response for GET /2/object/versionhistory/{pkiVersionhistoryID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**VersionhistoryGetObjectV2ResponseMPayload**](VersionhistoryGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.versionhistory_get_object_v2_response import VersionhistoryGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of VersionhistoryGetObjectV2Response from a JSON string
versionhistory_get_object_v2_response_instance = VersionhistoryGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print VersionhistoryGetObjectV2Response.to_json()

# convert the object into a dict
versionhistory_get_object_v2_response_dict = versionhistory_get_object_v2_response_instance.to_dict()
# create an instance of VersionhistoryGetObjectV2Response from a dict
versionhistory_get_object_v2_response_form_dict = versionhistory_get_object_v2_response.from_dict(versionhistory_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


