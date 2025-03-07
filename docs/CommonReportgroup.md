# CommonReportgroup

A group of reports  Each Reportgroup is for a specific recipient or for a specific context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_report** | [**List[CommonReport]**](CommonReport.md) |  | 
**a_obj_reportcellstyle_custom** | [**List[CommonReportcellstyle]**](CommonReportcellstyle.md) |  | 
**a_obj_reportgroup_parameter** | [**List[CommonReportgroupParameter]**](CommonReportgroupParameter.md) |  | 
**s_reportgroup_filename** | **str** | The name of the file | 

## Example

```python
from eZmaxApi.models.common_reportgroup import CommonReportgroup

# TODO update the JSON string below
json = "{}"
# create an instance of CommonReportgroup from a JSON string
common_reportgroup_instance = CommonReportgroup.from_json(json)
# print the JSON string representation of the object
print(CommonReportgroup.to_json())

# convert the object into a dict
common_reportgroup_dict = common_reportgroup_instance.to_dict()
# create an instance of CommonReportgroup from a dict
common_reportgroup_from_dict = CommonReportgroup.from_dict(common_reportgroup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


