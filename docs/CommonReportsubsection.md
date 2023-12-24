# CommonReportsubsection

A Subsection in a Reportsection. It contains 3 Reportsubsectionparts (Header, Body and Footer) 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_reportsubsectionpart_header** | [**CommonReportsubsectionpart**](CommonReportsubsectionpart.md) |  | 
**obj_reportsubsectionpart_body** | [**CommonReportsubsectionpart**](CommonReportsubsectionpart.md) |  | 
**obj_reportsubsectionpart_footer** | [**CommonReportsubsectionpart**](CommonReportsubsectionpart.md) |  | 

## Example

```python
from eZmaxApi.models.common_reportsubsection import CommonReportsubsection

# TODO update the JSON string below
json = "{}"
# create an instance of CommonReportsubsection from a JSON string
common_reportsubsection_instance = CommonReportsubsection.from_json(json)
# print the JSON string representation of the object
print CommonReportsubsection.to_json()

# convert the object into a dict
common_reportsubsection_dict = common_reportsubsection_instance.to_dict()
# create an instance of CommonReportsubsection from a dict
common_reportsubsection_form_dict = common_reportsubsection.from_dict(common_reportsubsection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


