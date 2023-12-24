# CommonReportrow

A row in a Reportsubsectionpart 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_reportcell** | [**List[CommonReportcell]**](CommonReportcell.md) |  | 
**i_reportrow_height** | **int** | The reportrow height in pixels | 

## Example

```python
from eZmaxApi.models.common_reportrow import CommonReportrow

# TODO update the JSON string below
json = "{}"
# create an instance of CommonReportrow from a JSON string
common_reportrow_instance = CommonReportrow.from_json(json)
# print the JSON string representation of the object
print CommonReportrow.to_json()

# convert the object into a dict
common_reportrow_dict = common_reportrow_instance.to_dict()
# create an instance of CommonReportrow from a dict
common_reportrow_form_dict = common_reportrow.from_dict(common_reportrow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


