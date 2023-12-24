# EzsigntemplatesignatureCreateObjectV1Request

Request for POST /1/object/ezsigntemplatesignature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatesignature** | [**List[EzsigntemplatesignatureRequestCompound]**](EzsigntemplatesignatureRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_create_object_v1_request import EzsigntemplatesignatureCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureCreateObjectV1Request from a JSON string
ezsigntemplatesignature_create_object_v1_request_instance = EzsigntemplatesignatureCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatesignatureCreateObjectV1Request.to_json()

# convert the object into a dict
ezsigntemplatesignature_create_object_v1_request_dict = ezsigntemplatesignature_create_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplatesignatureCreateObjectV1Request from a dict
ezsigntemplatesignature_create_object_v1_request_form_dict = ezsigntemplatesignature_create_object_v1_request.from_dict(ezsigntemplatesignature_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


