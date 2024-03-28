# EzsigntemplatedocumentEditObjectV1Request

Request for PUT /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatedocument** | [**EzsigntemplatedocumentRequestCompound**](EzsigntemplatedocumentRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_edit_object_v1_request import EzsigntemplatedocumentEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentEditObjectV1Request from a JSON string
ezsigntemplatedocument_edit_object_v1_request_instance = EzsigntemplatedocumentEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentEditObjectV1Request.to_json())

# convert the object into a dict
ezsigntemplatedocument_edit_object_v1_request_dict = ezsigntemplatedocument_edit_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplatedocumentEditObjectV1Request from a dict
ezsigntemplatedocument_edit_object_v1_request_form_dict = ezsigntemplatedocument_edit_object_v1_request.from_dict(ezsigntemplatedocument_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


