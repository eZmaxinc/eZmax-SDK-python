# EzsigntemplatesignatureCreateObjectV3Request

Request for POST /3/object/ezsigntemplatesignature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatesignature** | [**List[EzsigntemplatesignatureRequestCompoundV2]**](EzsigntemplatesignatureRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_create_object_v3_request import EzsigntemplatesignatureCreateObjectV3Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureCreateObjectV3Request from a JSON string
ezsigntemplatesignature_create_object_v3_request_instance = EzsigntemplatesignatureCreateObjectV3Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureCreateObjectV3Request.to_json())

# convert the object into a dict
ezsigntemplatesignature_create_object_v3_request_dict = ezsigntemplatesignature_create_object_v3_request_instance.to_dict()
# create an instance of EzsigntemplatesignatureCreateObjectV3Request from a dict
ezsigntemplatesignature_create_object_v3_request_from_dict = EzsigntemplatesignatureCreateObjectV3Request.from_dict(ezsigntemplatesignature_create_object_v3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


