# CommonReport

A Report containing Reportsections 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_reportsection** | [**List[CommonReportsection]**](CommonReportsection.md) |  | 
**b_report_paginate** | **bool** | Whether we display pagination in the report | [optional] 
**s_report_title** | **str** | The title of this Report | [optional] 

## Example

```python
from eZmaxApi.models.common_report import CommonReport

# TODO update the JSON string below
json = "{}"
# create an instance of CommonReport from a JSON string
common_report_instance = CommonReport.from_json(json)
# print the JSON string representation of the object
print(CommonReport.to_json())

# convert the object into a dict
common_report_dict = common_report_instance.to_dict()
# create an instance of CommonReport from a dict
common_report_from_dict = CommonReport.from_dict(common_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


