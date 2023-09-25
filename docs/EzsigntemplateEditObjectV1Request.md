# EzsigntemplateEditObjectV1Request

Request for PUT /1/object/ezsigntemplate/{pkiEzsigntemplateID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplate** | [**EzsigntemplateRequestCompound**](EzsigntemplateRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_edit_object_v1_request import EzsigntemplateEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateEditObjectV1Request from a JSON string
ezsigntemplate_edit_object_v1_request_instance = EzsigntemplateEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateEditObjectV1Request.to_json()

# convert the object into a dict
ezsigntemplate_edit_object_v1_request_dict = ezsigntemplate_edit_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplateEditObjectV1Request from a dict
ezsigntemplate_edit_object_v1_request_form_dict = ezsigntemplate_edit_object_v1_request.from_dict(ezsigntemplate_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


