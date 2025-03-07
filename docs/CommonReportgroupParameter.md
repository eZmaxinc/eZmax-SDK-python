# CommonReportgroupParameter

A parameter of Reportgroup 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_reportgroup_parameter_name** | **str** | The Reportparameter name | 
**s_reportgroup_parameter_value** | **str** | The Reportparameter value | [optional] 
**a_s_reportgroup_parameter_value** | **List[str]** |  | [optional] 

## Example

```python
from eZmaxApi.models.common_reportgroup_parameter import CommonReportgroupParameter

# TODO update the JSON string below
json = "{}"
# create an instance of CommonReportgroupParameter from a JSON string
common_reportgroup_parameter_instance = CommonReportgroupParameter.from_json(json)
# print the JSON string representation of the object
print(CommonReportgroupParameter.to_json())

# convert the object into a dict
common_reportgroup_parameter_dict = common_reportgroup_parameter_instance.to_dict()
# create an instance of CommonReportgroupParameter from a dict
common_reportgroup_parameter_from_dict = CommonReportgroupParameter.from_dict(common_reportgroup_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


