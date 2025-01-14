# EzsigndocumentEditEzsignannotationsV1Request

Request for PUT /1/object/ezsigndocument/{pkiEzsigndocumentID}/editEzsignannotations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignannotation** | [**List[EzsignannotationRequestCompound]**](EzsignannotationRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_edit_ezsignannotations_v1_request import EzsigndocumentEditEzsignannotationsV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentEditEzsignannotationsV1Request from a JSON string
ezsigndocument_edit_ezsignannotations_v1_request_instance = EzsigndocumentEditEzsignannotationsV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentEditEzsignannotationsV1Request.to_json())

# convert the object into a dict
ezsigndocument_edit_ezsignannotations_v1_request_dict = ezsigndocument_edit_ezsignannotations_v1_request_instance.to_dict()
# create an instance of EzsigndocumentEditEzsignannotationsV1Request from a dict
ezsigndocument_edit_ezsignannotations_v1_request_from_dict = EzsigndocumentEditEzsignannotationsV1Request.from_dict(ezsigndocument_edit_ezsignannotations_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


