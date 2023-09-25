# CommonGetReportV1ResponseMPayload

Payload for POST /1/report/xxx/xxx and and /1/module/report/getReportFromCache

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_reportgroup** | [**CommonReportgroup**](CommonReportgroup.md) |  | 

## Example

```python
from eZmaxApi.models.common_get_report_v1_response_m_payload import CommonGetReportV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CommonGetReportV1ResponseMPayload from a JSON string
common_get_report_v1_response_m_payload_instance = CommonGetReportV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print CommonGetReportV1ResponseMPayload.to_json()

# convert the object into a dict
common_get_report_v1_response_m_payload_dict = common_get_report_v1_response_m_payload_instance.to_dict()
# create an instance of CommonGetReportV1ResponseMPayload from a dict
common_get_report_v1_response_m_payload_form_dict = common_get_report_v1_response_m_payload.from_dict(common_get_report_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


