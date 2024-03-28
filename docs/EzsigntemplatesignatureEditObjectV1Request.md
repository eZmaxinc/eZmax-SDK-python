# EzsigntemplatesignatureEditObjectV1Request

Request for PUT /1/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatesignature** | [**EzsigntemplatesignatureRequestCompound**](EzsigntemplatesignatureRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_edit_object_v1_request import EzsigntemplatesignatureEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureEditObjectV1Request from a JSON string
ezsigntemplatesignature_edit_object_v1_request_instance = EzsigntemplatesignatureEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureEditObjectV1Request.to_json())

# convert the object into a dict
ezsigntemplatesignature_edit_object_v1_request_dict = ezsigntemplatesignature_edit_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplatesignatureEditObjectV1Request from a dict
ezsigntemplatesignature_edit_object_v1_request_form_dict = ezsigntemplatesignature_edit_object_v1_request.from_dict(ezsigntemplatesignature_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


