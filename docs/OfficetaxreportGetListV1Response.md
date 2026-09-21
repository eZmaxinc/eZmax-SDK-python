# OfficetaxreportGetListV1Response

Response for GET /1/object/officetaxreport/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**OfficetaxreportGetListV1ResponseMPayload**](OfficetaxreportGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.officetaxreport_get_list_v1_response import OfficetaxreportGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of OfficetaxreportGetListV1Response from a JSON string
officetaxreport_get_list_v1_response_instance = OfficetaxreportGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(OfficetaxreportGetListV1Response.to_json())

# convert the object into a dict
officetaxreport_get_list_v1_response_dict = officetaxreport_get_list_v1_response_instance.to_dict()
# create an instance of OfficetaxreportGetListV1Response from a dict
officetaxreport_get_list_v1_response_from_dict = OfficetaxreportGetListV1Response.from_dict(officetaxreport_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


