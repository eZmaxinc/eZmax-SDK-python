# CommonReportsubsectionpart

A part in the Reportsubsection 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_reportsubsectionpart_type** | **str** | The type of the Reportsubsectionpart | 
**a_obj_reportrow** | [**List[CommonReportrow]**](CommonReportrow.md) |  | 
**a_s_variableobject_property** | **List[str]** |  | 

## Example

```python
from eZmaxApi.models.common_reportsubsectionpart import CommonReportsubsectionpart

# TODO update the JSON string below
json = "{}"
# create an instance of CommonReportsubsectionpart from a JSON string
common_reportsubsectionpart_instance = CommonReportsubsectionpart.from_json(json)
# print the JSON string representation of the object
print(CommonReportsubsectionpart.to_json())

# convert the object into a dict
common_reportsubsectionpart_dict = common_reportsubsectionpart_instance.to_dict()
# create an instance of CommonReportsubsectionpart from a dict
common_reportsubsectionpart_from_dict = CommonReportsubsectionpart.from_dict(common_reportsubsectionpart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


