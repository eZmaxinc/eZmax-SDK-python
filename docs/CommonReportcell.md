# CommonReportcell

A cell in a Reportrow 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_reportcell_columnspan** | **int** | The number of Reportcolumns the Reportcell spans | 
**i_reportcell_rowspan** | **int** | The number of Reportrows the Reportcell spans | 

## Example

```python
from eZmaxApi.models.common_reportcell import CommonReportcell

# TODO update the JSON string below
json = "{}"
# create an instance of CommonReportcell from a JSON string
common_reportcell_instance = CommonReportcell.from_json(json)
# print the JSON string representation of the object
print CommonReportcell.to_json()

# convert the object into a dict
common_reportcell_dict = common_reportcell_instance.to_dict()
# create an instance of CommonReportcell from a dict
common_reportcell_form_dict = common_reportcell.from_dict(common_reportcell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


