# EzsigndocumentApplyEzsigntemplateV1Request

Request for POST /1/object/ezsigndocument/{pkiEzsigndocumentID}/applyezsigntemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**a_s_ezsigntemplatesigner** | **List[str]** |  | 
**a_pki_ezsignfoldersignerassociation_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_apply_ezsigntemplate_v1_request import EzsigndocumentApplyEzsigntemplateV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentApplyEzsigntemplateV1Request from a JSON string
ezsigndocument_apply_ezsigntemplate_v1_request_instance = EzsigndocumentApplyEzsigntemplateV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentApplyEzsigntemplateV1Request.to_json())

# convert the object into a dict
ezsigndocument_apply_ezsigntemplate_v1_request_dict = ezsigndocument_apply_ezsigntemplate_v1_request_instance.to_dict()
# create an instance of EzsigndocumentApplyEzsigntemplateV1Request from a dict
ezsigndocument_apply_ezsigntemplate_v1_request_from_dict = EzsigndocumentApplyEzsigntemplateV1Request.from_dict(ezsigndocument_apply_ezsigntemplate_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


