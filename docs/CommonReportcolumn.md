# CommonReportcolumn

A column in a Reportsection 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_reportcellstyle_default** | [**CommonReportcellstyle**](CommonReportcellstyle.md) |  | 
**i_reportcolumn_width** | **int** | The Reportcolumn width in pixels | 

## Example

```python
from eZmaxApi.models.common_reportcolumn import CommonReportcolumn

# TODO update the JSON string below
json = "{}"
# create an instance of CommonReportcolumn from a JSON string
common_reportcolumn_instance = CommonReportcolumn.from_json(json)
# print the JSON string representation of the object
print CommonReportcolumn.to_json()

# convert the object into a dict
common_reportcolumn_dict = common_reportcolumn_instance.to_dict()
# create an instance of CommonReportcolumn from a dict
common_reportcolumn_form_dict = common_reportcolumn.from_dict(common_reportcolumn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


