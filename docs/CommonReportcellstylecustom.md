# CommonReportcellstylecustom

Styles applied to a Reportcell 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_reportcellstyle_bordertop** | **bool** | Whether there is a border at the top of the Reportcell | [optional] 
**b_reportcellstyle_borderbottom** | **bool** | Whether there is a border at the bottom of the Reportcell | [optional] 
**b_reportcellstyle_borderleft** | **bool** | Whether there is a border at the left of the Reportcell | [optional] 
**b_reportcellstyle_borderright** | **bool** | Whether there is a border at the right of the Reportcell | [optional] 
**e_reportcell_horizontalalignment** | [**EnumHorizontalalignment**](EnumHorizontalalignment.md) |  | [optional] 
**e_reportcell_verticalalignment** | [**EnumVerticalalignment**](EnumVerticalalignment.md) |  | [optional] 
**e_reportcell_fontweight** | [**EnumFontweight**](EnumFontweight.md) |  | [optional] 
**e_reportcell_fontunderline** | [**EnumFontunderline**](EnumFontunderline.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.common_reportcellstylecustom import CommonReportcellstylecustom

# TODO update the JSON string below
json = "{}"
# create an instance of CommonReportcellstylecustom from a JSON string
common_reportcellstylecustom_instance = CommonReportcellstylecustom.from_json(json)
# print the JSON string representation of the object
print(CommonReportcellstylecustom.to_json())

# convert the object into a dict
common_reportcellstylecustom_dict = common_reportcellstylecustom_instance.to_dict()
# create an instance of CommonReportcellstylecustom from a dict
common_reportcellstylecustom_from_dict = CommonReportcellstylecustom.from_dict(common_reportcellstylecustom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


