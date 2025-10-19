# EzsigntemplatedocumentEditEzsigntemplatesignaturesV2Request

Request for PUT /2/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/editEzsigntemplatesignatures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatesignature** | [**List[EzsigntemplatesignatureRequestCompound]**](EzsigntemplatesignatureRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_edit_ezsigntemplatesignatures_v2_request import EzsigntemplatedocumentEditEzsigntemplatesignaturesV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentEditEzsigntemplatesignaturesV2Request from a JSON string
ezsigntemplatedocument_edit_ezsigntemplatesignatures_v2_request_instance = EzsigntemplatedocumentEditEzsigntemplatesignaturesV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentEditEzsigntemplatesignaturesV2Request.to_json())

# convert the object into a dict
ezsigntemplatedocument_edit_ezsigntemplatesignatures_v2_request_dict = ezsigntemplatedocument_edit_ezsigntemplatesignatures_v2_request_instance.to_dict()
# create an instance of EzsigntemplatedocumentEditEzsigntemplatesignaturesV2Request from a dict
ezsigntemplatedocument_edit_ezsigntemplatesignatures_v2_request_from_dict = EzsigntemplatedocumentEditEzsigntemplatesignaturesV2Request.from_dict(ezsigntemplatedocument_edit_ezsigntemplatesignatures_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


