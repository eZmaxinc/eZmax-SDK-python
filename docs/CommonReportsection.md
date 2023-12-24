# CommonReportsection

A section in a Report. Each Reportsection shares Reportcolumns disposition with all its Reportsubsection 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_reportsubsection** | [**List[CommonReportsubsection]**](CommonReportsubsection.md) |  | 
**a_obj_reportcolumn** | [**List[CommonReportcolumn]**](CommonReportcolumn.md) |  | 
**e_reportsection_horizontalalignment** | [**EnumHorizontalalignment**](EnumHorizontalalignment.md) |  | 
**i_reportsection_columncount** | **int** | The number of Reportcolumns in the Reportsection | 
**i_reportsection_width** | **int** | The combined width of all the Reportcolumns in the Reportsection | 

## Example

```python
from eZmaxApi.models.common_reportsection import CommonReportsection

# TODO update the JSON string below
json = "{}"
# create an instance of CommonReportsection from a JSON string
common_reportsection_instance = CommonReportsection.from_json(json)
# print the JSON string representation of the object
print CommonReportsection.to_json()

# convert the object into a dict
common_reportsection_dict = common_reportsection_instance.to_dict()
# create an instance of CommonReportsection from a dict
common_reportsection_form_dict = common_reportsection.from_dict(common_reportsection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


