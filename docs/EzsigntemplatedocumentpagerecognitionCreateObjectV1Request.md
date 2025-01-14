# EzsigntemplatedocumentpagerecognitionCreateObjectV1Request

Request for POST /1/object/ezsigntemplatedocumentpagerecognition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatedocumentpagerecognition** | [**List[EzsigntemplatedocumentpagerecognitionRequestCompound]**](EzsigntemplatedocumentpagerecognitionRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocumentpagerecognition_create_object_v1_request import EzsigntemplatedocumentpagerecognitionCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentpagerecognitionCreateObjectV1Request from a JSON string
ezsigntemplatedocumentpagerecognition_create_object_v1_request_instance = EzsigntemplatedocumentpagerecognitionCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentpagerecognitionCreateObjectV1Request.to_json())

# convert the object into a dict
ezsigntemplatedocumentpagerecognition_create_object_v1_request_dict = ezsigntemplatedocumentpagerecognition_create_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplatedocumentpagerecognitionCreateObjectV1Request from a dict
ezsigntemplatedocumentpagerecognition_create_object_v1_request_from_dict = EzsigntemplatedocumentpagerecognitionCreateObjectV1Request.from_dict(ezsigntemplatedocumentpagerecognition_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


