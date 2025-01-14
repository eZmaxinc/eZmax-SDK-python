# EzsigntemplatesignatureCreateObjectV2Request

Request for POST /2/object/ezsigntemplatesignature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatesignature** | [**List[EzsigntemplatesignatureRequestCompoundV2]**](EzsigntemplatesignatureRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_create_object_v2_request import EzsigntemplatesignatureCreateObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureCreateObjectV2Request from a JSON string
ezsigntemplatesignature_create_object_v2_request_instance = EzsigntemplatesignatureCreateObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureCreateObjectV2Request.to_json())

# convert the object into a dict
ezsigntemplatesignature_create_object_v2_request_dict = ezsigntemplatesignature_create_object_v2_request_instance.to_dict()
# create an instance of EzsigntemplatesignatureCreateObjectV2Request from a dict
ezsigntemplatesignature_create_object_v2_request_from_dict = EzsigntemplatesignatureCreateObjectV2Request.from_dict(ezsigntemplatesignature_create_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


