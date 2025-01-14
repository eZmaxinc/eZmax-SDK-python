# EzsigntemplatedocumentpagerecognitionEditObjectV1Request

Request for PUT /1/object/ezsigntemplatedocumentpagerecognition/{pkiEzsigntemplatedocumentpagerecognitionID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatedocumentpagerecognition** | [**EzsigntemplatedocumentpagerecognitionRequestCompound**](EzsigntemplatedocumentpagerecognitionRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocumentpagerecognition_edit_object_v1_request import EzsigntemplatedocumentpagerecognitionEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentpagerecognitionEditObjectV1Request from a JSON string
ezsigntemplatedocumentpagerecognition_edit_object_v1_request_instance = EzsigntemplatedocumentpagerecognitionEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentpagerecognitionEditObjectV1Request.to_json())

# convert the object into a dict
ezsigntemplatedocumentpagerecognition_edit_object_v1_request_dict = ezsigntemplatedocumentpagerecognition_edit_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplatedocumentpagerecognitionEditObjectV1Request from a dict
ezsigntemplatedocumentpagerecognition_edit_object_v1_request_from_dict = EzsigntemplatedocumentpagerecognitionEditObjectV1Request.from_dict(ezsigntemplatedocumentpagerecognition_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


