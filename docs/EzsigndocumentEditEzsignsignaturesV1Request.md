# EzsigndocumentEditEzsignsignaturesV1Request

Request for PUT /1/object/ezsigndocument/{pkiEzsigndocumentID}/editEzsignsignatures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignsignature** | [**List[EzsignsignatureRequestCompound]**](EzsignsignatureRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_edit_ezsignsignatures_v1_request import EzsigndocumentEditEzsignsignaturesV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentEditEzsignsignaturesV1Request from a JSON string
ezsigndocument_edit_ezsignsignatures_v1_request_instance = EzsigndocumentEditEzsignsignaturesV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentEditEzsignsignaturesV1Request.to_json())

# convert the object into a dict
ezsigndocument_edit_ezsignsignatures_v1_request_dict = ezsigndocument_edit_ezsignsignatures_v1_request_instance.to_dict()
# create an instance of EzsigndocumentEditEzsignsignaturesV1Request from a dict
ezsigndocument_edit_ezsignsignatures_v1_request_from_dict = EzsigndocumentEditEzsignsignaturesV1Request.from_dict(ezsigndocument_edit_ezsignsignatures_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


