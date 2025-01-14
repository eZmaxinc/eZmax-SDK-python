# EzsignannotationEditObjectV1Request

Request for PUT /1/object/ezsignannotation/{pkiEzsignannotationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignannotation** | [**EzsignannotationRequestCompound**](EzsignannotationRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignannotation_edit_object_v1_request import EzsignannotationEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignannotationEditObjectV1Request from a JSON string
ezsignannotation_edit_object_v1_request_instance = EzsignannotationEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignannotationEditObjectV1Request.to_json())

# convert the object into a dict
ezsignannotation_edit_object_v1_request_dict = ezsignannotation_edit_object_v1_request_instance.to_dict()
# create an instance of EzsignannotationEditObjectV1Request from a dict
ezsignannotation_edit_object_v1_request_from_dict = EzsignannotationEditObjectV1Request.from_dict(ezsignannotation_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


