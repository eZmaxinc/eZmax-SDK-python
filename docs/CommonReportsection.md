# CommonReportsection

A section in a Report. Each Reportsection shares Reportcolumns disposition with all its Reportsubsection 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_reportsubsection** | [**List[CommonReportsubsection]**](CommonReportsubsection.md) |  | 
**e_reportsection_horizontalalignment** | [**EnumHorizontalalignment**](EnumHorizontalalignment.md) |  | 
**s_reportsection_title** | **str** | The title of this Reportsection | [optional] 
**s_reportsection_tabname** | **str** | The name of tab in excel version | [optional] 

## Example

```python
from eZmaxApi.models.common_reportsection import CommonReportsection

# TODO update the JSON string below
json = "{}"
# create an instance of CommonReportsection from a JSON string
common_reportsection_instance = CommonReportsection.from_json(json)
# print the JSON string representation of the object
print(CommonReportsection.to_json())

# convert the object into a dict
common_reportsection_dict = common_reportsection_instance.to_dict()
# create an instance of CommonReportsection from a dict
common_reportsection_from_dict = CommonReportsection.from_dict(common_reportsection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


