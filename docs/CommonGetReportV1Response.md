# CommonGetReportV1Response

Response for POST /1/report/xxx/xxx and /1/module/report/getReportFromCache

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CommonGetReportV1ResponseMPayload**](CommonGetReportV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.common_get_report_v1_response import CommonGetReportV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommonGetReportV1Response from a JSON string
common_get_report_v1_response_instance = CommonGetReportV1Response.from_json(json)
# print the JSON string representation of the object
print(CommonGetReportV1Response.to_json())

# convert the object into a dict
common_get_report_v1_response_dict = common_get_report_v1_response_instance.to_dict()
# create an instance of CommonGetReportV1Response from a dict
common_get_report_v1_response_from_dict = CommonGetReportV1Response.from_dict(common_get_report_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


