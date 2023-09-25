# VersionhistoryGetObjectV2ResponseMPayload

Payload for GET /2/object/versionhistory/{pkiVersionhistoryID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_versionhistory** | [**VersionhistoryResponseCompound**](VersionhistoryResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.versionhistory_get_object_v2_response_m_payload import VersionhistoryGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of VersionhistoryGetObjectV2ResponseMPayload from a JSON string
versionhistory_get_object_v2_response_m_payload_instance = VersionhistoryGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print VersionhistoryGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
versionhistory_get_object_v2_response_m_payload_dict = versionhistory_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of VersionhistoryGetObjectV2ResponseMPayload from a dict
versionhistory_get_object_v2_response_m_payload_form_dict = versionhistory_get_object_v2_response_m_payload.from_dict(versionhistory_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


