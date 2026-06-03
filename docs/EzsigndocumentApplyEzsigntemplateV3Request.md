# EzsigndocumentApplyEzsigntemplateV3Request

Request for POST /3/object/ezsigndocument/{pkiEzsigndocumentID}/applyezsigntemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**a_s_ezsigntemplatesigner** | **List[str]** |  | 
**a_fki_ezsignfoldersignerassociation_id** | **List[int]** |  | 
**a_s_ezsigntemplateannotation_description** | **List[str]** |  | 
**a_s_ezsigntemplateannotation_defaulttext** | **List[str]** |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_apply_ezsigntemplate_v3_request import EzsigndocumentApplyEzsigntemplateV3Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentApplyEzsigntemplateV3Request from a JSON string
ezsigndocument_apply_ezsigntemplate_v3_request_instance = EzsigndocumentApplyEzsigntemplateV3Request.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentApplyEzsigntemplateV3Request.to_json())

# convert the object into a dict
ezsigndocument_apply_ezsigntemplate_v3_request_dict = ezsigndocument_apply_ezsigntemplate_v3_request_instance.to_dict()
# create an instance of EzsigndocumentApplyEzsigntemplateV3Request from a dict
ezsigndocument_apply_ezsigntemplate_v3_request_from_dict = EzsigndocumentApplyEzsigntemplateV3Request.from_dict(ezsigndocument_apply_ezsigntemplate_v3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


