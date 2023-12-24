# CommonReportcellstyle

Styles applied to a Reportcell 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_reportcellstyle_bordertop** | **bool** | Whether there is a border at the top of the Reportcell | 
**b_reportcellstyle_borderbottom** | **bool** | Whether there is a border at the bottom of the Reportcell | 
**b_reportcellstyle_borderleft** | **bool** | Whether there is a border at the left of the Reportcell | 
**b_reportcellstyle_borderright** | **bool** | Whether there is a border at the right of the Reportcell | 
**e_reportcell_horizontalalignment** | [**EnumHorizontalalignment**](EnumHorizontalalignment.md) |  | 
**e_reportcell_verticalalignment** | [**EnumVerticalalignment**](EnumVerticalalignment.md) |  | 
**e_reportcell_fontweight** | [**EnumFontweight**](EnumFontweight.md) |  | 
**e_reportcell_fontunderline** | [**EnumFontunderline**](EnumFontunderline.md) |  | 

## Example

```python
from eZmaxApi.models.common_reportcellstyle import CommonReportcellstyle

# TODO update the JSON string below
json = "{}"
# create an instance of CommonReportcellstyle from a JSON string
common_reportcellstyle_instance = CommonReportcellstyle.from_json(json)
# print the JSON string representation of the object
print CommonReportcellstyle.to_json()

# convert the object into a dict
common_reportcellstyle_dict = common_reportcellstyle_instance.to_dict()
# create an instance of CommonReportcellstyle from a dict
common_reportcellstyle_form_dict = common_reportcellstyle.from_dict(common_reportcellstyle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


