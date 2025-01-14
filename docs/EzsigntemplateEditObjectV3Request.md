# EzsigntemplateEditObjectV3Request

Request for PUT /3/object/ezsigntemplate/{pkiEzsigntemplateID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplate** | [**EzsigntemplateRequestCompoundV3**](EzsigntemplateRequestCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_edit_object_v3_request import EzsigntemplateEditObjectV3Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateEditObjectV3Request from a JSON string
ezsigntemplate_edit_object_v3_request_instance = EzsigntemplateEditObjectV3Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateEditObjectV3Request.to_json())

# convert the object into a dict
ezsigntemplate_edit_object_v3_request_dict = ezsigntemplate_edit_object_v3_request_instance.to_dict()
# create an instance of EzsigntemplateEditObjectV3Request from a dict
ezsigntemplate_edit_object_v3_request_from_dict = EzsigntemplateEditObjectV3Request.from_dict(ezsigntemplate_edit_object_v3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


