# EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1Request

Request for PUT /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/editEzsigntemplatedocumentpagerecognitions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatedocumentpagerecognition** | [**List[EzsigntemplatedocumentpagerecognitionRequestCompound]**](EzsigntemplatedocumentpagerecognitionRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_edit_ezsigntemplatedocumentpagerecognitions_v1_request import EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1Request from a JSON string
ezsigntemplatedocument_edit_ezsigntemplatedocumentpagerecognitions_v1_request_instance = EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1Request.to_json())

# convert the object into a dict
ezsigntemplatedocument_edit_ezsigntemplatedocumentpagerecognitions_v1_request_dict = ezsigntemplatedocument_edit_ezsigntemplatedocumentpagerecognitions_v1_request_instance.to_dict()
# create an instance of EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1Request from a dict
ezsigntemplatedocument_edit_ezsigntemplatedocumentpagerecognitions_v1_request_from_dict = EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1Request.from_dict(ezsigntemplatedocument_edit_ezsigntemplatedocumentpagerecognitions_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


